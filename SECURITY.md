# Security policy — homelab documentation

This is a **public documentation and learning repository**. It does not provide a production service or promise a security support SLA.

## Sensitive information

Do not create issues or pull requests containing:

- Passwords, tokens, API keys, cookies or credential hashes
- VPN private keys, client QR codes or private configuration files
- Private user data, password vault content, backups or database dumps
- Raw logs that expose sensitive accounts, network endpoints or browsing history

The [screenshot checklist](docs/guides/screenshots.md) and [verification playbook](docs/guides/verification.md) describe how to sanitize evidence.

## Reporting a sensitive concern

If a repository file accidentally exposes a secret or sensitive infrastructure detail, avoid public disclosure. Use GitHub's private vulnerability reporting **if enabled** or contact the maintainer privately through the contact methods on the [GitHub profile](https://github.com/lilouwen).

Removing a file from the latest commit does not remove it from Git history. Compromised credentials should be revoked or rotated immediately, and remediation should account for the repository history.

## Scope

Infrastructure hardening guidance here is **not proof of a live security audit**. Validate deployed controls before presenting them as effective.

[← Repository home](README.md)
