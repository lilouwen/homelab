# Network ports

> **Documentation status:** This page reflects historical project notes. Recheck versions, ports and service states on the live host before updating statements of fact.

## Network Ports and Access

A documented listening port is not proof of Internet exposure. Actual access depends on the bind address, Docker publication, host firewall, Freebox rules, IPv6 routing and client network position. See [verification steps](guides/verification.md).

The following table documents the local services and their associated ports.

These addresses are private and are intended for access through the local network or VPN, subject to the configured security rules.

| Service | Port / Protocol | Purpose |
|---|---|---|
| SSH | `22/TCP` | Remote administration |
| Pi-hole DNS | `53/TCP`, `53/UDP` | DNS filtering |
| Pi-hole Web | `80/TCP` | DNS management interface |
| Homepage | `3000/TCP` | Homelab dashboard |
| Uptime Kuma | `3001/TCP` | Availability monitoring |
| Vaultwarden | `8080/TCP` | Password manager |
| Nextcloud | `8081/TCP` | Private cloud |
| Syncthing Web | `8384/TCP` | Synchronization management |
| Syncthing Sync | `22000` | File synchronization transport |
| Portainer | `9443/TCP` | Docker administration |
| Netdata | `19999/TCP` | System monitoring |
| WireGuard | `51820/UDP` | Remote VPN access |
| Samba | `445/TCP` | Windows file sharing |

**Important:** This table documents reported or expected port assignments. The current listening ports, Docker mappings, Syncthing transport configuration and Samba configuration must be checked on the server.

## Network Exposure Policy

The intended exposure model is:

- WireGuard provides the external remote access entry point.
- Web administration interfaces remain restricted to trusted networks.
- SSH is intended for authorized administration.
- DNS is provided to selected LAN and VPN clients.
- Database services are not intentionally published directly to the Internet.

The actual exposure must be verified against router rules, host firewall rules, Docker port publishing and IPv6 connectivity.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
