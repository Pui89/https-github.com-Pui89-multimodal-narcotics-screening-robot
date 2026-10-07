# Security

## Repository security

The repository uses dependency review, CodeQL, Dependabot configuration, CODEOWNERS, and a lightweight credential-pattern CI check.

These controls reduce risk but do not constitute a security certification.

## Runtime security principles

- Do not commit credentials, tokens, private keys, or personal data.
- Use least-privilege service accounts.
- Keep robot control isolated from model inference.
- Treat sensor data as potentially sensitive.
- Minimize retention and access to recorded imagery.
- Validate third-party models and dependencies before deployment.
- Keep emergency-stop and deterministic safety controls independent of foundation models.

Report suspected vulnerabilities privately through the repository's supported security reporting mechanism rather than publishing exploit details in an issue.
