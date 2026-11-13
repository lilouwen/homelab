# Pi-hole · DNS filtering / resolver

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Reported interface:** 53/TCP and 53/UDP; administration reportedly 80/TCP

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The original deployment notes describe Pi-hole as the selected DNS server for some LAN clients and for the WireGuard phone during an earlier mobile-network test. Current service availability has not been rechecked.

## 02 // Dependencies and design considerations

- Client DNS settings must point to a reachable DNS service.
- Port 53 must be reachable from the intended LAN and VPN clients; the administration interface should remain restricted.
- Pi-hole is not proven to be a Docker container by the recorded inventory.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Record the upstream DNS resolver without exposing account or network secrets.
- Compare DNS resolution on the LAN and through WireGuard.
- Confirm which interface the DNS and admin ports bind to.
- Check that unrestricted Internet hosts cannot use this resolver.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Inspect DNS listeners on the Linux host
sudo ss -lntup | grep -E '(:53[[:space:]]|:80[[:space:]])'
# See system resolver configuration
resolvectl status
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| LAN DNS | A permitted LAN client receives an answer from the intended resolver |
| VPN DNS | A connected VPN client uses the intended resolver |
| Filtered domain | Only domains configured for filtering are blocked |
| Public access | DNS and web administration are not unintentionally open to the Internet |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| No resolution | Check DHCP/DNS settings, resolver state and port 53 conflicts. |
| VPN DNS fails | Check WireGuard peer DNS settings, routes and firewall rules. |
| Web UI unavailable | Confirm service binding and expected internal access path. |

## 05 // Security and data protection

- Preserve sanitized list/group policy documentation.
- Include Pi-hole configuration in the proposed backup plan, but mark the scheduled job unverified.
- Test restore on an isolated or appropriately protected environment.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [wireguard](wireguard.md)
- [docker](docker.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
