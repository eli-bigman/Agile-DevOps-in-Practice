# Health Check API - Final Project

## Overview

This project is a Health Check API built with Python (FastAPI) demonstrating Agile & DevOps practices including CI/CD, automated testing, and iterative delivery.

## Key Deliverables

- **Source Code**: [src/](src/)
- **Tests**: [tests/](tests/)
- **CI/CD**: [.github/workflows/ci-pipeline.yml](.github/workflows/ci-pipeline.yml)

## Sprint Artifacts

- **Sprint 0 (Planning)**: [sprints/sprint-0.md](sprints/sprint-0.md)
- **Sprint 1 (Review)**: [sprints/sprint-1-review.md](sprints/sprint-1-review.md)
- **Sprint 1 (Retro)**: [sprints/sprint-1-retrospective.md](sprints/sprint-1-retrospective.md)
- **Sprint 2 (Review)**: [sprints/sprint-2-review.md](sprints/sprint-2-review.md)
- **Sprint 2 (Retro)**: [sprints/sprint-2-retrospective.md](sprints/sprint-2-retrospective.md)

## How to Run Locally

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Start server:
    ```bash
    uvicorn src.main:app --reload
    ```
3.  Visit docs: [http://localhost:8000/docs](http://localhost:8000/docs)
