# Pi-hole

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Function:** DNS filtering  
**Reported access / ports:** 53/TCP and UDP; UI 80/TCP

## Purpose

DNS, filtering and query monitoring.

## Documented project notes

Pi-hole provides DNS-based filtering for devices configured to use the homelab DNS server.

Its main functions include:

- DNS query processing.
- Domain-based filtering.
- Advertisement and tracking domain blocking.
- DNS activity statistics.
- Filtering for VPN clients.

The documented configuration uses the Linux server as a DNS endpoint for selected devices.

> Historical deployment notes are not a live validation. Do not publish credentials, keys, tokens, private files or identifying screenshots.

## Validation checklist

- [ ] Verify the service is installed and its current runtime state
- [ ] Confirm listening interfaces, ports and network access
- [ ] Review permissions, authentication and secret handling
- [ ] Add a redacted screenshot or configuration example once verified

## Related documents

- [Network architecture](../network-architecture.md)
- [Network ports](../network-ports.md)
- [Security & hardening](../security.md)
- [Backup & recovery](../backup-recovery.md)

---

[← Service directory](README.md) · [Repository home](../../README.md)
