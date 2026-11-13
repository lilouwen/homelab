# WireGuard

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Networking & security  
**Function:** Encrypted VPN  
**Reported access / ports:** 51820/UDP

## Purpose

Secure remote access from approved clients.

## Documented project notes

Remote access is provided through a WireGuard VPN tunnel.

WireGuard allows authorized devices to communicate with internal homelab services while avoiding intentional direct Internet exposure of application administration interfaces.

## VPN Configuration

| Parameter | Value |
|---|---|
| VPN Technology | WireGuard |
| Transport | UDP |
| Listening Port | `51820` |
| VPN Server | `10.7.0.1/24` |
| Documented Mobile Client | `10.7.0.2/24` |
| VPN Network | `10.7.0.0/24` |

The Freebox forwards UDP port `51820` to the VPN server.

## Remote Connection Flow

```mermaid
flowchart LR
    A["Remote Device"]
    B["Internet"]
    C["Freebox"]
    D["WireGuard VPN"]
    E["Internal Services"]

    A --> B
    B --> C
    C -->|"UDP 51820"| D
    D --> E

    classDef vpn fill:#302b63,stroke:#818cf8,color:#ffffff
    class A,B,C,D,E vpn
```

### Documented Connectivity Test

A remote connection test was performed using a mobile phone over a 4G/5G network.

The recorded results indicate:

- Successful WireGuard handshake.
- Traffic transmitted and received through the tunnel.
- Access to internal resources.
- DNS filtering through Pi-hole while connected to the VPN.

These observations come from the deployment documentation and should be revalidated after configuration changes.

### Security Principle

Only authorized VPN peers should be allowed to access the private infrastructure.

Application access remains subject to local firewall rules and service-specific authentication.

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
