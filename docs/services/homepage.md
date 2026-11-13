# Homepage · Internal service portal

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Reported interface:** 3000/TCP (documented)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

Homepage is documented as the central dashboard for navigation to homelab applications. A container named homepage appears in the previously recorded inventory.

## 02 // Dependencies and design considerations

- Service tiles are convenience links, not independent security controls.
- Any widget API integration can require a token; those tokens must be protected.
- Exposed tiles may disclose hostnames or service endpoints even if access itself is restricted.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Validate tile URLs, availability and the actual published host port.
- Redact access details and integrations before sharing dashboard screenshots.
- Check that portal visibility is limited to permitted LAN/VPN clients.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check container and published ports
sudo docker ps --filter 'name=homepage' --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Dashboard access | Authorized LAN/VPN client can load the portal |
| Links | Tiles navigate to expected local services |
| Sensitive information | No credential, API token or remote public endpoint is shown |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Blank dashboard | Container logs, configuration syntax and mounted files. |
| Widget not updating | Service reachability, API permissions and network policy. |
| Tile unreachable | Target service state, DNS and internal port mapping. |

## 05 // Security and data protection

- Version sanitized dashboard structure only after removing secrets.
- Store real token-bearing configuration privately.
- Provide screenshots only after reviewing metadata and visible URLs.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [docker](docker.md)
- [portainer](portainer.md)
- [uptime-kuma](uptime-kuma.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
