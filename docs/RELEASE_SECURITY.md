# Release security

Tagged releases should include Python wheel/source distribution, SHA-256 checksums, an SBOM, signed artifact attestation and build provenance.

Verify a published artifact with:
gh attestation verify dist/<artifact> -R Pui89/multimodal-narcotics-screening-robot

Never publish secrets, private keys, personal data or raw sensitive sensor recordings in release artifacts.
