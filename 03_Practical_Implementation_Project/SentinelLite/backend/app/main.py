
from fastapi import FastAPI, File, HTTPException, UploadFile

from backend.app.detection_engine import detect_security_alerts
from backend.app.log_parser import parse_security_logs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SentinelLite API",
    description="A rule-based security log analysis API.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "SentinelLite",
        "version": "1.0.0",
    }



MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


@app.post("/api/analyze")
async def analyze_logs(file: UploadFile = File(...)):
    """Upload a size-limited CSV file and return validation results."""

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file.",
        )

    try:
        content = await file.read(MAX_FILE_SIZE + 1)

        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413,
                detail="File too large. Maximum allowed size is 5 MB.",
            )

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty.",
            )

        csv_content = content.decode("utf-8-sig")
        result = parse_security_logs(csv_content)
        alerts = detect_security_alerts(result["valid_rows"])

        return {
            "filename": file.filename,
            "summary": {
                "total_rows": result["total_rows"],
                "valid_rows": result["valid_count"],
                "invalid_rows": result["invalid_count"],
                "alerts_detected": len(alerts),
            },
            "invalid_rows": result["invalid_rows"],
            "alerts": alerts,
        }

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="File must use UTF-8 text encoding.",
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    finally:
        await file.close()

