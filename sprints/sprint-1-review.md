# Sprint 1 Review

## Goal

To deliver the first increment of working software (Health API) and establish the DevOps pipeline.

## Delivered User Stories

| ID       | Story                    | Status   | Evidence                                                                  |
| :------- | :----------------------- | :------- | :------------------------------------------------------------------------ |
| **US-1** | Basic `/health` endpoint | **Done** | Endpoint returns `200 OK` and `"status": "ok"`. Verified via local test.  |
| **US-4** | Timestamp in response    | **Done** | JSON response includes valid ISO 8601 timestamp. Verified via local test. |
| **US-3** | API Versioning           | **Done** | Implemented as V1 (implicit in structure).                                |

## Demo / Validation

- **Endpoint URL:** `http://localhost:8000/health`
- **Sample Response:**
  ```json
  {
    "status": "ok",
    "timestamp": "2023-10-27T10:00:00+00:00"
  }
  ```
- **CI/CD Pipeline:** functional on GitHub Actions (triggers on push to `master`).
- **Testing:** `pytest` passing for checking status code and payload structure.

## Screenshots

- ![ Screenshot of GitHub Actions "Green" Build](sprint1-review.png)
