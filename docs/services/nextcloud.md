# Nextcloud · Self-hosted cloud and files

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** 8081/TCP (historical mapping)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The recorded Docker inventory lists nextcloud with nextcloud-db (MariaDB) and nextcloud-redis (Redis). Current versions, data locations and HTTPS configuration are not verified.

## 02 // Dependencies and design considerations

- Nextcloud uses application data and configuration in addition to its database.
- MariaDB and Redis are internal dependencies; the records do not show them publicly exposed.
- A reverse proxy/HTTPS migration is planned, not confirmed as deployed.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Identify the existing app, data and database volumes before changing anything.
- Review trusted domains, HTTPS, reverse proxy and access policy.
- Verify that DB/Redis have no unintended host publication.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Inspect recorded containers and their current state
sudo docker ps -a --filter 'name=nextcloud' --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
# Nextcloud occ is optional: only after confirming the image/container and user
sudo docker exec -u www-data nextcloud php occ status
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Application reachability | Authorized client reaches login via permitted network |
| Database dependency | Application can access its DB without external exposure |
| Redis dependency | Configured cache/locking works as intended |
| Backup restore | App + data + DB restore to a coherent state |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Internal server error | Application logs, database connectivity, permissions, app maintenance state. |
| Slow file operations | HDD I/O, available RAM, database and locking/cache configuration. |
| Broken links/redirects | Trusted domains, reverse proxy headers and HTTPS settings. |

## 05 // Security and data protection

- Back up Nextcloud files, configuration and MariaDB using a consistent process.
- Test restore with the matching application version and required service dependencies.
- Never publish documents, database exports or real configuration secrets.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [mariadb](mariadb.md)
- [redis](redis.md)
- [docker](docker.md)
- [vaultwarden](vaultwarden.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
