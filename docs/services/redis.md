# Redis · Nextcloud supporting cache/locking

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** No host-published Redis port documented

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The historical Docker inventory includes nextcloud-redis. The precise role, Redis persistence mode and authentication/network settings need confirmation against the live Nextcloud configuration.

## 02 // Dependencies and design considerations

- Nextcloud may use Redis for caching or transactional file locking; check the actual configuration.
- Redis should not be reachable over the public Internet.
- Cache state and application data have different backup requirements.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Verify container health, image version and internal network binding.
- Check the actual Nextcloud integration and intended cache/locking role.
- Verify no public host port mapping exists.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Inventory Redis container and mapped ports
sudo docker ps -a --filter 'name=nextcloud-redis' --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| App connectivity | Nextcloud reaches Redis when configured to use it |
| Network isolation | No unnecessary Redis listener on publicly reachable interfaces |
| Failure handling | Expected behavior during a planned Redis outage is understood |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Connection refused | Container state, Docker network, service name and port. |
| Memory pressure | Redis limits, host RAM, workload and memory eviction configuration. |
| App warning | Check Nextcloud Redis settings and available logs. |

## 05 // Security and data protection

- Determine whether Redis contains only regenerable cache or also data requiring persistence.
- Never publish authentication configuration or dumps.
- Prioritize application database and file backups for Nextcloud restoration.

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
- [mariadb](mariadb.md)
- [docker](docker.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
