# Samba · Authenticated Windows file sharing

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Reported interface:** 445/TCP typical; confirm effective listeners

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The prior deployment notes describe an authenticated SMB share for Windows clients, with guest access disabled. The current export configuration has not been retrieved.

## 02 // Dependencies and design considerations

- Filesystem permissions and Samba share permissions must both authorize the intended users.
- Windows clients must have a network path and compatible SMB dialect.
- Network policy should restrict file sharing to trusted LAN/VPN clients.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Review the effective share list, path permissions and guest access.
- Verify SMB dialects and disable outdated/unused access paths according to the host requirements.
- Test both authorized and unauthorized clients.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Validate Samba configuration syntax and report effective shares
sudo testparm -s
# Inspect SMB listeners
sudo ss -lntp | grep ':445'
# Check active Samba connections (sensitive: redact before sharing)
sudo smbstatus
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Authorized access | Permitted Windows account can read/write as intended |
| Guest access | Unauthenticated clients cannot browse restricted shares |
| Access boundary | SMB is unavailable from non-trusted networks |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Share not visible | Client discovery, SMB service and network path. |
| Authentication rejected | Account mapping and Samba user state. |
| Permission denied | Unix file permissions, ACLs and Samba share restrictions. |

## 05 // Security and data protection

- Important shared files require independent, versioned backups.
- Do not treat Syncthing/Nextcloud synchronization as backup.
- Record access-control decisions without publishing usernames or sensitive folder names.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [syncthing](syncthing.md)
- [nextcloud](nextcloud.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
