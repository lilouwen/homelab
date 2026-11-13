# MariaDB · Nextcloud relational database

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** No host-published database port documented

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The existing Docker inventory identifies the nextcloud-db container. It is associated with Nextcloud; the exact MariaDB version, credentials and internal network are not documented.

## 02 // Dependencies and design considerations

- Nextcloud relies on a correctly configured and reachable database.
- Data must be persisted independently of the application container lifecycle.
- Database consistency is important for safe backup and recovery.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Identify the database image/version, storage volume and actual container name.
- Confirm the DB is reachable only from intended application network contexts.
- Plan database-consistent backups without hardcoding credentials.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Locate the database container without printing credentials
sudo docker ps -a --filter 'name=nextcloud-db' --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Application connection | Nextcloud establishes a database connection |
| Network boundary | Database port is not unintentionally published |
| Restoration | A sanitized, isolated recovery test succeeds |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Authentication error | Credentials/permissions (never paste actual values), application config. |
| Data corruption warnings | Backups, storage health, clean shutdown and application logs. |
| Slow queries | Host HDD I/O, available memory and index/query patterns. |

## 05 // Security and data protection

- Use a supported logical dump or consistent database-aware backup method.
- Do not assume that copying an actively changing Docker volume is consistent.
- Encrypt copies containing private database records and test recovery.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [nextcloud](nextcloud.md)
- [redis](redis.md)
- [docker](docker.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
