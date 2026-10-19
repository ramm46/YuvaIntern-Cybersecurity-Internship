
import csv
import io
from typing import Any


REQUIRED_COLUMNS = {
    "event_id",
    "timestamp",
    "event_type",
    "source",
    "actor",
    "action",
    "outcome",
}

OPTIONAL_COLUMNS = {
    "source_ip",
    "details",
}

ALLOWED_COLUMNS = REQUIRED_COLUMNS | OPTIONAL_COLUMNS

# Prevent individual CSV fields from becoming excessively large.
MAX_CSV_FIELD_SIZE = 100_000


def parse_security_logs(csv_content: str) -> dict[str, Any]:
    """
    Parse and validate CSV security logs.

    Invalid individual rows are skipped and reported.
    Invalid file structure or missing required columns rejects the file.
    """
    if not csv_content or not csv_content.strip():
        raise ValueError("CSV file is empty.")
    
    previous_field_limit = csv.field_size_limit()
    csv.field_size_limit(MAX_CSV_FIELD_SIZE)

    
    try:
        reader = csv.DictReader(io.StringIO(csv_content, newline=""))
        headers = reader.fieldnames

        if not headers:
            raise ValueError("CSV header row is missing.")

        headers = [header.strip() for header in headers]

        if any(not header for header in headers):
            raise ValueError("CSV contains an empty column name.")

        if len(headers) != len(set(headers)):
            raise ValueError("CSV contains duplicate column names.")

        missing_columns = REQUIRED_COLUMNS - set(headers)
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {missing}")

        unexpected_columns = set(headers) - ALLOWED_COLUMNS
        if unexpected_columns:
            unexpected = ", ".join(sorted(unexpected_columns))
            raise ValueError(f"Unexpected columns: {unexpected}")

        reader.fieldnames = headers

        valid_rows = []
        invalid_rows = []

        for row_number, row in enumerate(reader, start=2):
            if None in row:
                invalid_rows.append({
                    "row_number": row_number,
                    "reason": "Row contains more values than the header.",
                })
                continue

            if any(value is None for value in row.values()):
                invalid_rows.append({
                    "row_number": row_number,
                    "reason": "Row contains missing values.",
                })
                continue

            normalized_row = {
                key: value.strip()
                for key, value in row.items()
            }

            empty_required = [
                column
                for column in REQUIRED_COLUMNS
                if not normalized_row.get(column, "")
            ]

            if empty_required:
                invalid_rows.append({
                    "row_number": row_number,
                    "reason": (
                        "Missing required values: "
                        + ", ".join(sorted(empty_required))
                    ),
                })
                continue

            valid_rows.append(normalized_row)

        return {
            "valid_rows": valid_rows,
            "invalid_rows": invalid_rows,
            "total_rows": len(valid_rows) + len(invalid_rows),
            "valid_count": len(valid_rows),
            "invalid_count": len(invalid_rows),
        }

    except csv.Error as exc:
        if "field larger than field limit" in str(exc):
            raise ValueError(
                f"CSV field exceeds the maximum allowed size "
                f"of {MAX_CSV_FIELD_SIZE} characters."
            ) from exc

        raise ValueError(f"Invalid CSV structure: {exc}") from exc
    finally:
        csv.field_size_limit(previous_field_limit)

