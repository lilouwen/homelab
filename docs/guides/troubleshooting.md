# Troubleshooting runbook

[← Documentation index](../README.md) · [← Repository](../../README.md)

**Method:** Confirm the symptom, identify the failing layer, gather minimal evidence, change one variable at a time and document the actual result. Avoid speculative edits to production services.

## Investigation sequence

1. **Client** — Are we on LAN, VPN or an untrusted external network?
2. **Resolution** — Does DNS resolve to the expected internal address?
3. **Transport** — Does the required TCP/UDP port accept traffic along the intended path?
4. **Host** — Is the Linux service/process healthy and bound to the expected interface?
5. **Container** — Is the Docker application running, and are its networks, dependencies and mounts correct?
6. **Application** — What do application logs show, after secrets are redacted?
7. **Storage and performance** — Is the HDD saturated, disk full or RAM under pressure?

## Common symptoms

| Observation | Narrow the problem |
|---|---|
| VPN handshake fails | Endpoint, forwarding, path and peer configuration |
| VPN connects but service unavailable | Return route, firewall, Docker binding or application ACL |
| Service resolves on LAN but not over VPN | DNS assignment, routing and VPN DNS policy |
| Web UI not reachable | Listener, container state, port publishing, TLS |
| Nextcloud errors | App logs, MariaDB/Redis, storage permissions, resource pressure |
| Vaultwarden inaccessible | TLS and application container, then host/network path |
| SMB permission denied | Samba share authorization and filesystem permissions |
| Slow application response | HDD I/O, RAM, swap and database load |
| Monitoring reports false downtime | Probe path, target, timeout and DNS |

## Safe evidence collection

```bash
# Host load and storage
uptime
free -h
df -h

# TCP/UDP listeners (redact sensitive info before sharing)
sudo ss -lntup

# Docker container overview
sudo docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

Prefer a short sanitized observation over full copies of configuration files or logs.

## Change and rollback discipline

- Record the existing state and expected impact.
- Prefer reversible changes and one change per test.
- Never disable a working remote SSH access path before testing the replacement.
- Do not delete Docker volumes to solve a startup error without a verified recovery plan.
- For stateful services, confirm backup integrity before upgrades.

[Lab journal template](../../journal/README.md) · [Verification checklist](verification.md)
