# Sprint 1 Retrospective

## Summary

Successfully established the project foundation, implemented the first health check endpoint, and set up the CI/CD pipeline. Encountered a minor configuration issue with branch naming but resolved it quickly.

## What went well?

- **Fast Setup:** FastAPI project structure was initialized quickly and efficiently.
- **Testing:** Integration tests were written immediately, ensuring the endpoint works as expected.
- **Clean Code:** Followed PEP8 standards and kept the code modular.

## What could be improved?

- **CI Configuration:** Initially configured the CI pipeline for `main` instead of `master`, which prevented the action from running on the first push. Fixed by updating the YAML file.
- **Documentation:** Could add more comments to the test files to explain _why_ we are testing certain fields.

## Action Items for Sprint 2

1.  **Strict Branching:** Ensure all feature work is done on `dev` or feature branches before merging to `master`.
2.  **Enhanced Logging:** As we add system metrics, we need better logging to debug potential issues.
