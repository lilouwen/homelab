# Security & hardening

> **Documentation status:** This page reflects historical project notes. Recheck versions, ports and service states on the live host before updating statements of fact.

## Security and Hardening

Security is a core objective of the homelab.

The infrastructure is designed to provide remote access while limiting unnecessary service exposure.

## Documented Security Measures

| Control | Description |
|---|---|
| WireGuard | Encrypted remote access tunnel |
| Fail2ban | Authentication abuse protection |
| SSH | Remote administration with authentication |
| Private Network | Internal access to application services |
| Samba Authentication | Restricted file share access |
| Vaultwarden | Protected administration credentials |
| DNS Filtering | Pi-hole filtering and logging |

## Current Security Approach

**Network Access**

The intended configuration uses WireGuard as the primary remote access method.

Internal application management interfaces are not deliberately exposed directly to the Internet.

**Authentication**

Sensitive services require authenticated access.

Samba is documented as requiring an authorized user, with guest access disabled.

**Host Protection**

Fail2ban is used to help protect SSH against repeated authentication attempts.

**Credential Protection**

Passwords, VPN private keys, tokens and other secrets are excluded from public documentation.

## Security design review

| Risk | Design intent | Evidence still needed |
|---|---|---|
| Unintended public service exposure | VPN-gated management interfaces | Router, IPv4/IPv6, Docker port and firewall audit |
| SSH credential attacks | Fail2ban and stronger SSH authentication | Effective SSH config, jail status and permitted source networks |
| Exposed private files | Authentication and restricted access | Samba ACL test; Nextcloud/Vaultwarden access check |
| Configuration leakage | Keep secrets outside public repository | Redaction review and private credential storage |
| Single host or HDD failure | Verified recoverable independent backups | Scheduled job check and restore test |

[Verification playbook](guides/verification.md) · [Backup restoration test](guides/backup-restore-test.md)

## Security Improvements

Planned improvements include:

- [ ] Verify all exposed TCP and UDP ports.
- [ ] Review Freebox port forwarding rules.
- [ ] Review IPv6 exposure.
- [ ] Audit Docker published ports.
- [ ] Verify host firewall rules.
- [ ] Configure SSH key-only authentication.
- [ ] Disable SSH password authentication after validating key access.
- [ ] Implement HTTPS for sensitive web applications.
- [ ] Review container permissions and isolation.
- [ ] Maintain regular security updates.
- [ ] Document security tests and their results.

### HTTPS and Reverse Proxy

A future objective is to implement HTTPS for internal services through a reverse proxy.

This will improve web interface security, particularly for sensitive applications such as Vaultwarden and Nextcloud.

Certificate validation and trusted access from authorized devices will form part of this deployment.

---

## Repository Security

This repository is intended for technical documentation and sanitized configuration examples.

Sensitive information must never be committed to the repository.

## Excluded Information

- Passwords.
- Private SSH keys.
- WireGuard private keys.
- WireGuard configuration files containing secrets.
- VPN QR codes.
- API tokens.
- `.env` files.
- Vaultwarden administration secrets.
- Database credentials.
- Database exports containing personal data.
- Backup archives.
- Public IP addresses and sensitive access details.

Configuration examples should use placeholders rather than real credentials.

Screenshots must be reviewed before publication to remove sensitive information.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
