# Fail2ban · Authentication failure protection

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Reported interface:** No service port expected for administrative access

> **Status: historical documentation.** The host is not available for a live check. No assertion below verifies that this service is currently running or secure.

## 01 // Purpose

The deployment report describes Fail2ban as active and enabled at startup, particularly for SSH protection. This is historical documentation and not a current health check.

## 02 // Dependencies and design considerations

- Relevant authentication logs must be available to the jail.
- Enforcement depends on an appropriate firewall backend and correct jail configuration.
- Fail2ban does not prevent every credential attack or substitute for restricted exposure.

## 03 // Observability and verification

**Questions to resolve when the homelab is back online:**

- Verify enabled jails, log sources, failure thresholds and ban duration.
- Confirm legitimate administration cannot be unexpectedly locked out.
- Review journal entries and firewall integration.

### Read-only inspection commands

These are candidate commands for a future authorized local check. Some tools or service names may be absent depending on deployment method; do not treat their output as already collected.

```bash
# Check service status
systemctl is-active fail2ban
# List active jails
sudo fail2ban-client status
# Check the SSH jail only if one is actually configured
sudo fail2ban-client status sshd
```

**Do not publish unredacted command output:** logs and diagnostics may include internal addresses, account names, peer identifiers or configuration details.

### Acceptance tests

| Check | Expected/interpretation |
|---|---|
| Jail loaded | Configured jail shows an operational status |
| Log matching | Expected authentication failures appear in the monitored source |
| Enforcement | Firewall integration and ban state are consistent with the policy |

## 04 // Troubleshooting

| Symptom | Diagnostic direction |
|---|---|
| No jails | Configuration not loaded, package/service issue or a parsing error. |
| No bans despite failures | Log path/backend, filter pattern or threshold mismatch. |
| Authorized user banned | Check allowed-source policy and authentication failure causes. |

## 05 // Security and data protection

- Keep sanitized jail overrides and rationale.
- Never copy real authentication logs containing sensitive identifiers into public Git.
- Record package/version dependencies during future validation.

See [Security & hardening](../security.md) and [Backup & recovery](../backup-recovery.md) for cross-service requirements.

## 06 // Implementation evidence to add

- [ ] Date of latest successful test and software version
- [ ] Sanitized screenshots (only if useful)
- [ ] Verified deployment type and actual listeners
- [ ] Port restrictions, service dependencies and restart behavior
- [ ] Recovery procedure and tested outcome, if stateful

The tracking workflow is described in [Verification playbook](../guides/verification.md).

## Related services

- [openssh](openssh.md)
- [wireguard](wireguard.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
