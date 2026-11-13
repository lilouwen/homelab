# Backup & recovery

## Backup and Recovery

Backup reliability is essential because the infrastructure currently relies on a single physical machine and storage device.

## Planned Backup Schedule

The following schedule was proposed in the deployment documentation.

Its execution, timezone configuration and recovery reliability have not yet been fully validated.

| Scheduled Time | Service | Data |
|---|---|---|
| `03:00` | Vaultwarden | Docker volume |
| `03:10` | WireGuard | VPN configuration |
| `03:20` | Pi-hole | DNS configuration |
| `03:30` | Backup Rotation | Archives older than 14 days |

## Backup Organization

A proposed local directory structure is:

```text
backups/
├── vaultwarden/
├── wireguard/
└── pihole/
```

This structure represents the planned backup organization, not proof that the jobs are currently running.

## Backup Strategy

The backup process should provide:

- Scheduled execution.
- Restricted access to archives.
- Protection of sensitive configuration files.
- Defined retention policies.
- Consistent database backups.
- Independent storage copies.
- Recovery testing.

## Recovery Improvements

- [ ] Validate automated backup execution.
- [ ] Validate archive retention.
- [ ] Test Vaultwarden recovery.
- [ ] Test WireGuard recovery.
- [ ] Test Pi-hole recovery.
- [ ] Back up Nextcloud configuration and data.
- [ ] Implement consistent MariaDB backups.
- [ ] Back up important Samba files.
- [ ] Store encrypted backup copies outside the server.
- [ ] Perform a complete recovery test.

### Important Limitation

Backups stored on the same physical HDD do not protect against disk failure.

Syncthing and Nextcloud synchronization also do not replace independent versioned backups.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
