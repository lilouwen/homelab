# Verification & evidence playbook

[← Documentation index](../README.md) · [← Repository](../../README.md)

**Goal:** Inspect the real deployment, correct stale documentation and collect safe evidence once the homelab is powered on. None of these commands has been executed for this documentation update.

## Safety before running checks

- Run on a system you own or administer, from an authorized local or VPN session.
- Start with read-only commands; avoid changing firewalls, ports, service credentials or volumes during evidence collection.
- Store command outputs privately. Redact internal identifiers, endpoints, private files and tokens before publishing.
- Do not post full WireGuard configuration, `wg show` peer endpoints, `docker inspect` environment variables or private application logs.

## Phase A — Host inventory

```bash
# Confirm actual OS and kernel
cat /etc/os-release
uname -r

# Resources and storage
free -h
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
df -h

# Network interfaces and routes (redact before publication)
ip -br address
ip route
```

**Record:** observed OS version, CPU/memory/disk constraints, network interfaces and any mismatch with [Hardware](../hardware.md).

## Phase B — Service and port inventory

```bash
# Service manager status; some units may not exist in this deployment
systemctl is-active docker ssh fail2ban wg-quick@wg0

# Published TCP/UDP listeners
sudo ss -lntup

# Docker inventory, including stopped containers
sudo docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
sudo docker network ls
sudo docker volume ls
sudo docker compose ls
```

**Record:** service name, state, image/version if available, bind address, reported port, intended audience and actual reachability. Do **not** publish full environment variables or container inspection dumps.

## Phase C — Network boundary checks

- Confirm the Freebox forwarding list, including IPv4 and IPv6 rules.
- Review the host firewall implementation in use (`ufw`, `nftables`, or another mechanism).
- Check whether Docker published ports bypass assumptions about host firewall policy.
- Verify DNS from a LAN client and a WireGuard peer.
- Test an intended management UI from an authorized client, then confirm it is unavailable from an unauthorized external path.

## Phase D — VPN checks

- From a remote client on mobile data, confirm handshake, permitted internal access and DNS.
- Avoid exposing private keys, QR codes and peer endpoints.
- Verify that `AllowedIPs`, forwarding and firewall policy work together as intended.
- Record the result and date in the [lab journal](../../journal/README.md).

## Phase E — Monitoring and backups

- Reconcile actual Uptime Kuma targets against the documented list.
- Review Netdata CPU, RAM, disk I/O and network charts.
- Check whether planned backups run successfully and whether they are copied off-host.
- Perform a recovery test before marking backups verified: [Restore test](backup-restore-test.md).

## Evidence record template

| Field | Example of what to record |
|---|---|
| Date | YYYY-MM-DD |
| Host / service | Name without sensitive hostname |
| Configuration claim | e.g. SSH listening only on planned interfaces |
| Verification method | Read-only command or authorized UI test |
| Observation | Sanitized summary, not raw secrets |
| Result | PASS / FAIL / NOT TESTED |
| Next action | Correct configuration or update documentation |

Only update a service page from **historical** to **verified** after the corresponding evidence exists.
