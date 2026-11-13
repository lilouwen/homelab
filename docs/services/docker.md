# Docker · Container runtime and deployment inventory

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** Published ports vary by container

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The previously recorded containers are homepage, nextcloud, nextcloud-db, nextcloud-redis, vaultwarden, uptime-kuma and portainer. This list is historical; current running states are unknown.

## 02 // Dependencies and design considerations

- Containers may depend on host storage, Docker networks, database services and published ports.
- Docker-published ports can expose services outside an assumed host-firewall boundary.
- Stateful services need consistent volume/database backups, not only image redeployment.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Rebuild an inventory of containers and their images, networks, health and resource usage.
- Review host port bindings including 0.0.0.0 and IPv6.
- Document Compose stacks only after redacting all secrets and identifiers.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Inventory of running and stopped containers
sudo docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
# List networks and volume names
sudo docker network ls
sudo docker volume ls
# Check Compose projects where supported
sudo docker compose ls
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Container inventory | Listed containers match the actual installation |
| Internal dependencies | Nextcloud can reach its database and Redis |
| Port boundaries | Only intended host interfaces accept published ports |
| Restart | Declared restart policies behave as expected after maintenance |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Container crash loop | Logs, image compatibility, file permissions and environment (redact secrets). |
| Port conflict | Another host process/container already listens on the port. |
| Storage issue | Volume mounts, free space and permissions; inspect before removing any volume. |

## 05 // Security and data protection

- Back up definitions separately from secrets.
- Use application-consistent database dumps where necessary.
- Test redeployment in a controlled environment before treating it as recovery.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [portainer](portainer.md)
- [nextcloud](nextcloud.md)
- [vaultwarden](vaultwarden.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
