# Secure release flow

1. Pull request: tests, lint, CodeQL and dependency review.
2. Main branch: reproducible validation and security checks.
3. Version tag: build wheel/source artifacts.
4. Generate SHA-256 checksums and SPDX SBOM.
5. Create signed provenance and SBOM attestations.
6. Publish release artifacts and generated notes.
7. Verify artifacts with GitHub CLI before deployment.

Workflow permissions are explicitly least-privilege. Artifact attestations use OIDC and should be verified by consumers.
