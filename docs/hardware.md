# Hardware & system

> **Documentation status:** This page reflects historical project notes. Recheck versions, ports and service states on the live host before updating statements of fact.

## Hardware and System

## Server Specifications

The homelab runs on a repurposed ASUS laptop connected to the local network through Ethernet.

| Component | Specification |
|---|---|
| Hardware | ASUS Laptop |
| Processor | Dual-Core CPU |
| Memory | 6 GB RAM |
| Storage | Approximately 686 GB HDD |
| Operating System | Xubuntu 26.04 LTS (reported; version not rechecked) |
| Connection | Ethernet |
| Local IP | `192.168.1.187` |
| Gateway | Freebox — `192.168.1.254` |
| VPN Subnet | `10.7.0.0/24` |

The laptop has been repurposed to provide an always-available local infrastructure without requiring dedicated enterprise server hardware.

Xubuntu provides a graphical environment for local maintenance, while daily administration is primarily performed remotely using SSH.

### Infrastructure Constraints

The hardware introduces several limitations:

- Limited CPU resources.
- 6 GB of available memory.
- HDD storage performance constraints.
- Single-machine dependency.
- No hardware redundancy.

These constraints make resource management, monitoring and backup procedures essential parts of the project.

---

## Results and Limitations

## Documented Results

The project demonstrates the reuse of consumer hardware to build a self-hosted infrastructure.

The deployment documentation covers:

- Linux server administration.
- Local DNS filtering.
- VPN remote access.
- Self-hosted cloud storage.
- Password management.
- Docker container administration.
- Network file sharing.
- File synchronization.
- Service availability monitoring.
- Host performance monitoring.

## Technical Challenges

### Limited Hardware Resources

The server operates with a dual-core CPU, 6 GB of RAM and HDD storage.

Resource-intensive services such as databases and cloud applications can place significant pressure on the hardware.

### Storage Performance

The HDD is identified as a major potential performance bottleneck.

Migrating to an SSD is a priority for improving application responsiveness and disk I/O performance.

### Single Point of Failure

All services depend on one physical machine.

Hardware failure, power loss or storage corruption can affect the entire infrastructure.

### Backup Resilience

Local backup procedures still require validation and an independent storage destination.

### Network Security

The intended LAN/VPN access model still requires verification of actual firewall, router, Docker and IPv6 exposure.

## Lessons Learned

This homelab provides practical experience in:

- Infrastructure design.
- Network service deployment.
- Linux administration.
- Container management.
- Secure remote connectivity.
- Troubleshooting.
- Resource monitoring.
- Infrastructure documentation.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
