# Monitoring

> **Documentation status:** This page reflects historical project notes. Recheck versions, ports and service states on the live host before updating statements of fact.

## Monitoring

Monitoring is used to evaluate service availability, system resource consumption and infrastructure health.

## Uptime Kuma

Uptime Kuma provides service availability monitoring.

The documented monitoring targets include:

- Pi-hole.
- Portainer.
- Vaultwarden.
- Netdata.
- Nextcloud.
- SSH.
- Freebox.

### Monitoring Objectives

- Detect service unavailability.
- Monitor response times.
- Maintain availability history.
- Identify recurring failures.
- Configure notifications for important incidents.

## Netdata

Netdata provides infrastructure performance monitoring.

Key metrics include:

| Metric | Purpose |
|---|---|
| CPU Usage | Monitor processor utilization |
| RAM Usage | Identify memory pressure |
| Swap Usage | Detect memory limitations |
| Disk I/O | Analyze storage bottlenecks |
| Disk Usage | Monitor available storage |
| Network Traffic | Analyze network activity |
| System Load | Evaluate host performance |
| Processes | Identify resource-intensive applications |

### Hardware Monitoring Focus

Because the server relies on an HDD and has only 6 GB of RAM, storage I/O and memory consumption are especially important.

These measurements can help determine when hardware upgrades become necessary.

## Signals to investigate

| Signal | Potential interpretation | Investigation |
|---|---|---|
| Uptime Kuma reports repeated failures | Network path or service outage | Check target-specific connectivity and application logs |
| Sustained memory pressure / swap activity | Insufficient RAM for workload | Review container memory and process usage |
| High HDD I/O wait | Disk throughput bottleneck | Compare application workload and disk metrics |
| DNS monitor failures | DNS service or path issue | Test resolver from relevant LAN/VPN clients |

Recorded monitoring targets are not guarantees of current monitor configuration. Capture baseline measurements only after the server is available.

## Monitoring Improvements

- [ ] Enable critical service notifications.
- [ ] Document monitoring thresholds.
- [ ] Add sanitized dashboard screenshots.
- [ ] Record baseline CPU and RAM usage.
- [ ] Measure disk I/O under load.
- [ ] Document service incident scenarios.
- [ ] Evaluate additional security monitoring.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
