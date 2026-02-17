# Sprint 2 Retrospective (Final)

## Summary

Successfully implemented advanced features (System Stats, Error Handling) and adhered to the new Git branching strategy (`dev` -> `master`). The application is now observable and robust.

## What went well?

- **Git Workflow:** Strict adherence to `dev` branch for features prevented direct commits to `master`, ensuring a stable main branch.
- **Library Integration:** `psutil` was straightforward to implement for system metrics.
- **Code Structure:** Extracting logic into `utils/` kept `main.py` clean.

## What could be improved?

- **Test Coverage:** Exception handling logic relies on integration tests; unit tests for the handler itself could be more beneficial.
- **Automation:** Pre-commit hooks for linting would save CI failures.

## Final Reflection

The project evolved from a simple concept to a production-ready API through iterative sprints. The CI/CD pipeline provided confidence in every change, and the structured backlog kept the team focused on value delivery.
