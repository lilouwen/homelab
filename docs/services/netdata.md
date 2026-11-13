# Netdata · CPU / memory / disk / network metrics

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Monitoring  
**Reported interface:** 19999/TCP (historical mapping)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The existing README describes Netdata monitoring CPU, RAM, swap, HDD I/O, disk, network traffic, processes and load. The active deployment method and listening interface require verification.

## 02 // Dependencies and design considerations

- The HDD and 6 GB RAM make storage I/O and memory utilization important.
- Resource telemetry does not replace application availability checks from Uptime Kuma.
- Publicly exposed metrics can reveal host and process information.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Verify whether Netdata is a system service or container on this host.
- Capture a baseline after the homelab has stabilized under normal workload.
- Restrict dashboard access to intended LAN/VPN clients.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check possible host installation
systemctl is-active netdata
# Check a possible container installation
sudo docker ps -a --filter 'name=netdata' --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
# Inspect the reported listener
sudo ss -lntp | grep ':19999'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| CPU/memory charts | Graphs update with the current host metrics |
| Disk I/O | Read/write activity visible and correlates with storage workloads |
| Access model | Metrics interface unavailable to unauthorized clients |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Blank charts | Collector health, privileges and data-source access. |
| Very high disk wait | Storage saturation, Nextcloud/database workload and HDD health. |
| UI unavailable | Service state, listener and firewall rules. |

## 05 // Security and data protection

- Keep only sanitized performance captures in Git.
- Config backup if custom alarms and collector overrides are important.
- Document baseline measurements without exposing host identifiers.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [uptime-kuma](uptime-kuma.md)
- [docker](docker.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
