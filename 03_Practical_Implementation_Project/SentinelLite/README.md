
# SentinelLite
### Lightweight Security Log Analysis and Alert Dashboard

SentinelLite is a security log analysis project designed to parse CSV-based security events, identify selected suspicious activities, and present generated alerts through an interactive dashboard.

## Project Objectives

- Analyze structured security logs uploaded as CSV files.
- Detect selected suspicious login and privilege-change activities.
- Display alert severity, metrics, and investigation details.
- Filter alerts and export filtered results for further analysis.
- Demonstrate a lightweight security monitoring workflow.

## Features

- **CSV Log Upload:** Upload supported security log CSV files.
- **Input Validation:** Reject unsupported files and invalid CSV structures.
- **Detection Engine:** Apply three detection rules to identify selected suspicious activities.
- **Alert Dashboard:** View alert counts, severity summaries, and timelines.
- **Filtering:** Filter alerts by available severity and other dashboard criteria.
- **Investigation Panel:** Inspect individual alert details.
- **CSV Export:** Export filtered alerts for further review.

## Detection Rules

| Rule ID | Detection                   | Severity |
|---------|-----------------------------|----------|
| DET-01  | Brute-Force Detection       | Medium   |
| DET-02  | Suspicious Successful Login | High     |
| DET-03  | Unapproved Privilege Change | Medium   |

### DET-01 — Brute-Force Detection
Identifies repeated failed login attempts. The current rule uses a threshold of five failed login attempts within a 10-minute window.

### DET-02 — Suspicious Successful Login
Identifies a successful login following at least five failed login attempts within a 10-minute window.

### DET-03 — Unapproved Privilege Change
Identifies privilege-change events from actors outside the configured privileged-actor allowlist.

The current allowlist includes `admin` and `security_admin`. Detection results depend on the input log fields and the configured rule logic.

## Technology Stack

### Backend
- Python
- FastAPI
- Pytest

### Frontend
- Next.js
- React
- TypeScript
- ESLint

### Data Input
- CSV security logs

## Project Structure

```text
SentinelLite/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── detection_engine.py
│   │   └── log_parser.py
│   └── tests/
├── data/
├── docs/
├── frontend-app/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
├── reports/
├── screenshots/
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

Install the following before running the application:

- Python with pip
- Node.js and npm
- Git

## Run Locally

Run the backend and frontend in separate terminals.

### 1. Start the Backend

From the `SentinelLite` directory:

```powershell
python -m uvicorn backend.app.main:app --reload
```

The backend should start at:

`http://127.0.0.1:8000`

### 2. Start the Frontend

Open a second terminal:

```powershell
cd frontend-app
npm install
npm run dev
```

Open the dashboard:

`http://localhost:3000`

### 3. Stop the Development Servers

Press `Ctrl + C` in each terminal when finished.

## Run Tests

From the `SentinelLite` directory:

```powershell
python -m pytest backend\tests -v
```

The test suite has previously reported **16 passed tests** covering API behavior, CSV validation, detection rules, and log parsing.

Run the frontend checks from the `frontend-app` directory:

```powershell
npm run lint
npm run build
```

These checks have also completed successfully in the development environment.

## Security Considerations

- Use synthetic or appropriately sanitized logs for demonstrations.
- Never commit API keys, passwords, tokens, or private environment files.
- Validate uploaded files before processing them.
- Review the backend configuration before exposing the service publicly.
- Configure appropriate CORS restrictions, access controls, request limits, and production error handling before deployment.
- Detection results are rule-based indicators and should be reviewed before treating an event as a confirmed incident.

## Documentation

Project documentation is available in the `docs/` directory, including:

- Project Proposal
- Requirements Specification (SRS)
- Architecture and Data Specification
- Data Specification
- Development Plan
- Threat Model

## Current Status

- Backend test suite: 16 tests passed in the latest local verification.
- Frontend lint: completed successfully.
- Frontend production build: completed successfully.
- Local dashboard workflow: CSV upload, detection rules, severity filters, investigation panel, and CSV export verified.

## Limitations

SentinelLite currently analyzes uploaded CSV logs using its configured detection rules. It should not be considered a replacement for a production SIEM or a continuously operating security monitoring service.

## Disclaimer

SentinelLite is an educational security monitoring project. Use it only with logs you are authorized to analyze.
