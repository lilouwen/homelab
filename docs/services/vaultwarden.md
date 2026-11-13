# Vaultwarden · Password vault

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** 8080/TCP (historical mapping)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

Vaultwarden is recorded as a container for Bitwarden-compatible clients. Previous notes mention an Argon2id-hashed administration token; neither the token nor its hash should appear in Git.

## 02 // Dependencies and design considerations

- Account data and encryption-sensitive metadata require strict backup privacy.
- Using a credential vault over plain HTTP can be unsafe even if access is private; internal HTTPS is a priority for validation.
- Administrative access must be restricted and audited.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Verify the accessible endpoint and confirm HTTPS/trusted client behavior.
- Review who can access the admin interface and account registration policy.
- Identify the persistent database/data volume and a secure backup method.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check the Vaultwarden container and network mappings
sudo docker ps -a --filter 'name=vaultwarden' --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Client login | Expected authorized client can authenticate over a trusted secure connection |
| Admin security | Administrative interface is access-controlled |
| Restore | Encrypted backup restores to an isolated test instance |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Cannot connect | Container availability, internal DNS, TLS and network policy. |
| Login fails | Client/server version compatibility and credential policy. |
| Database issue | Volume permissions and consistent backup state. |

## 05 // Security and data protection

- Secure, encrypted, versioned backup of Vaultwarden data is important.
- Never publish the database, real secrets or Argon2id administration hash.
- Test recovery without revealing user vault contents.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [docker](docker.md)
- [portainer](portainer.md)
- [nextcloud](nextcloud.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
