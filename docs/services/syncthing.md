# Syncthing · Peer-to-peer file synchronization

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Reported interface:** Web UI 8384/TCP; synchronization port 22000 (transport to verify)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

Syncthing is mentioned as a file synchronization service complementing Nextcloud. The active peers, discovery settings and transport modes are not documented.

## 02 // Dependencies and design considerations

- Each participant must be authorized and its synchronized folders correctly scoped.
- Synchronization can propagate changes/deletions and is not the same as independent backup.
- Web administration should remain behind an appropriate trusted boundary.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Identify the actual process or container deployment method.
- Review peer authorization and folder share permissions.
- Verify the Web UI binding and enabled sync transports.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check whether a local Syncthing process exists
pgrep -af syncthing
# Inspect likely ports (actual protocols may differ)
sudo ss -lntup | grep -E '(:8384|:22000)'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Peer authorization | Only intended peers can synchronize |
| File update | A harmless test file synchronizes as expected |
| Deletion handling | Versioning/retention policy is understood and tested |
| Web UI access | Administration is limited to trusted clients |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Peer disconnected | Peer IDs, discovery, firewall and relaying policy. |
| Folder out of sync | Permissions, disk capacity, conflict files and ignore patterns. |
| No web UI | Listening interface or service/container status. |

## 05 // Security and data protection

- Use independent backups for source data; sync alone is insufficient.
- Review file-versioning options where needed.
- Never include personal synchronized data in public documentation.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [samba](samba.md)
- [nextcloud](nextcloud.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
