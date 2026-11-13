# Uptime Kuma · Service availability checks

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Monitoring  
**Reported interface:** 3001/TCP (historical mapping)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The previous documentation lists Pi-hole, Portainer, Vaultwarden, Netdata, Nextcloud, SSH and Freebox among the monitored services. Current probes and notifications have not been checked.

## 02 // Dependencies and design considerations

- Probes show perspective-specific availability, not proof of service security.
- Alerts require notification channels to be configured and tested.
- Local monitoring on the same host will fail to report outages if the host is down unless external monitoring is available.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Verify monitor names, types, timeouts and polling intervals.
- Identify notifications and run a non-destructive test alert.
- Distinguish LAN-only, VPN-only and application-health checks.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Confirm monitor container and reported host-port binding
sudo docker ps -a --filter 'name=uptime-kuma' --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Probe status | A known available service passes the configured check |
| Alerting | Test notification reaches the recipient |
| Real failure | A controlled maintenance window produces expected detection |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| False negative | Monitor host reachability, DNS/TLS chain and timeout. |
| Missing notifications | Provider token, notification method, retry settings and test button. |
| Unexpected green state | Check whether probe hits the real application endpoint rather than a generic port. |

## 05 // Security and data protection

- Protect monitoring configuration/state if useful for incident history.
- Do not publish notification secrets or internal URLs embedded in monitor definitions.
- Use sanitized screenshots for the public showcase.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [netdata](netdata.md)
- [homepage](homepage.md)
- [docker](docker.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
