# OpenSSH · Remote system administration

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Reported interface:** 22/TCP (reported)

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

SSH is documented as the principal remote administration method for the Xubuntu server. Key-only authentication is an improvement objective, not a confirmed current setting.

## 02 // Dependencies and design considerations

- A working authorized administrative account and network path are required.
- Fail2ban can complement but does not replace strong authentication and firewall controls.
- The SSH listener should be reachable only from intended management networks.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Keep a second authorized session open when changing SSH authentication.
- Verify key-based login before disabling password authentication.
- Inspect effective SSH settings and access rules, not only the configuration file.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check whether the SSH service is active
systemctl is-active ssh
# Check listeners (review output before sharing)
sudo ss -lntp | grep ':22'
# Inspect effective authentication settings
sudo sshd -T | grep -E '^(passwordauthentication|pubkeyauthentication|permitrootlogin)'
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Authorized login | Known authorized key/account can open a session |
| Unauthorized access | Rejected as intended by the effective policy |
| Management path | SSH accessible through only the planned network paths |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| Connection refused | Service down, wrong port or listener binding. |
| Timeout | Routing, host firewall or router filtering. |
| Permission denied | Account state, authorized keys, file permissions or SSH config. |

## 05 // Security and data protection

- Preserve a sanitized record of effective SSH policy.
- Back up host config securely; never publish private keys.
- Document a rollback plan before disabling an access method.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [fail2ban](fail2ban.md)
- [wireguard](wireguard.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
