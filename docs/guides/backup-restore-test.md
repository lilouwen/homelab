# Backup and restore verification

[← Documentation index](../README.md) · [← Repository](../../README.md)

**Status:** The recorded 03:00–03:30 backup schedule is a proposal. Execution and restore success have not been verified.

## Principles

A backup strategy needs **recovery evidence**, not just scheduled files. One hard drive is a single point of failure, and synchronization alone is not a backup.

- Keep copies separate from the server, ideally with an encrypted off-host destination.
- Handle databases with a consistency-aware procedure.
- Restrict permissions on backups of VPN keys, password vaults and application credentials.
- Restore into an isolated environment, not on top of live data.

## Systems requiring consideration

| System | Recovery scope |
|---|---|
| Vaultwarden | Encrypted application database/data volume and relevant configuration |
| WireGuard | Protected keys, network policy and peer assignments |
| Pi-hole | DNS settings, filter rules/lists and local customizations |
| Nextcloud | Files, application configuration and MariaDB state |
| MariaDB | Database-consistent dump / restore |
| Samba | Important shared files and permissions |
| Docker | Compose definitions, intended networks, volume mapping information |

## Example non-production restore test

1. Select one small service and record the intended backup source.
2. Confirm an independently stored archive exists, can be read and is appropriately protected.
3. Prepare an isolated recovery destination with no conflicting ports or real accounts.
4. Restore the application data and configuration in the expected order.
5. Confirm service starts and an authorized harmless test operation works.
6. Check data integrity and access controls after restore.
7. Record the date, scope, application versions, time taken and whether recovery succeeded.
8. Remove the temporary test environment securely.

**Do not use production secrets in screenshots or commit backups to Git.**

## Completion criteria

- [ ] Backups actually run on schedule
- [ ] Failures notify the operator
- [ ] External encrypted copy exists
- [ ] Retention is confirmed
- [ ] Restore has been tested
- [ ] Recovery notes are available
- [ ] Test results recorded without confidential material

[Backup plan](../backup-recovery.md) · [Lab journal](../../journal/README.md)
