<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=210&section=header&text=LILOUWEN%20HOMELAB&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="LILOUWEN HOMELAB"/></p>

<h3 align="center">NETWORK INFRASTRUCTURE · LINUX · SELF-HOSTING · SECURITY</h3>
<p align="center">An ASUS laptop repurposed as a personal Linux server.<br/>A hands-on lab for network services, containers, secure remote access and monitoring.</p>

---

## Project overview

This repository documents a self-hosted homelab for learning **network engineering, Linux administration, automation and cybersecurity**.

**The documented setup is not a live status page.** The host is currently offline and its precise OS version, exposed ports, service states and scheduled backups still need revalidation.

## Network at a glance

```mermaid
flowchart TB
    R["Remote device"] --> I["Internet"]
    I --> F["Freebox router"]
    L["Local devices"] --> F
    F -->|"Ethernet / LAN"| S["ASUS Xubuntu host"]
    F -->|"UDP 51820 VPN forwarding"| W["WireGuard"]
    W -.-> S
    S --> D["Docker applications"]
    S --> N["DNS / SSH / File services"]
    S --> M["Monitoring"]
    classDef edge fill:#17213a,stroke:#64748b,color:#fff
    classDef host fill:#302b63,stroke:#818cf8,color:#fff
    classDef app fill:#153b57,stroke:#38bdf8,color:#fff
    class R,I,F,L edge
    class W,S host
    class D,N,M app
```

[**Explore the full network topology**](docs/network-architecture.md) · [**Network access & ports**](docs/network-ports.md)

## Service directory

**Click any service badge to open its dedicated technical page.** These badges identify technologies; they do not report live health.

### Networking & security

<p align="center">
  <a href="docs/services/pi-hole.md"><img src="https://img.shields.io/badge/Pi--hole-DNS%20filtering-96060C?style=for-the-badge&logo=pihole&logoColor=white" alt="Pi-hole · DNS filtering"/></a>
  <a href="docs/services/wireguard.md"><img src="https://img.shields.io/badge/WireGuard-Encrypted%20VPN-88171A?style=for-the-badge&logo=wireguard&logoColor=white" alt="WireGuard · Encrypted VPN"/></a>
  <a href="docs/services/openssh.md"><img src="https://img.shields.io/badge/OpenSSH-SSH%20administration-2671BE?style=for-the-badge&logo=openssh&logoColor=white" alt="OpenSSH · SSH administration"/></a>
  <a href="docs/services/fail2ban.md"><img src="https://img.shields.io/badge/Fail2ban-Authentication%20defense-7C3AED?style=for-the-badge&logo=linux&logoColor=white" alt="Fail2ban · Authentication defense"/></a>
  <a href="docs/services/samba.md"><img src="https://img.shields.io/badge/Samba-Network%20file%20sharing-C2185B?style=for-the-badge&logo=samba&logoColor=white" alt="Samba · Network file sharing"/></a>
  <a href="docs/services/syncthing.md"><img src="https://img.shields.io/badge/Syncthing-File%20synchronization-0891B2?style=for-the-badge&logo=syncthing&logoColor=white" alt="Syncthing · File synchronization"/></a>
</p>

### Containers & applications

<p align="center">
  <a href="docs/services/docker.md"><img src="https://img.shields.io/badge/Docker-Container%20runtime-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker · Container runtime"/></a>
  <a href="docs/services/portainer.md"><img src="https://img.shields.io/badge/Portainer-Docker%20administration-13BEF9?style=for-the-badge&logo=portainer&logoColor=white" alt="Portainer · Docker administration"/></a>
  <a href="docs/services/homepage.md"><img src="https://img.shields.io/badge/Homepage-Application%20portal-6366F1?style=for-the-badge&logo=homepage&logoColor=white" alt="Homepage · Application portal"/></a>
  <a href="docs/services/nextcloud.md"><img src="https://img.shields.io/badge/Nextcloud-Private%20cloud-0082C9?style=for-the-badge&logo=nextcloud&logoColor=white" alt="Nextcloud · Private cloud"/></a>
  <a href="docs/services/mariadb.md"><img src="https://img.shields.io/badge/MariaDB-Database-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB · Database"/></a>
  <a href="docs/services/redis.md"><img src="https://img.shields.io/badge/Redis-Application%20cache-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis · Application cache"/></a>
  <a href="docs/services/vaultwarden.md"><img src="https://img.shields.io/badge/Vaultwarden-Password%20vault-175DDC?style=for-the-badge&logo=bitwarden&logoColor=white" alt="Vaultwarden · Password vault"/></a>
</p>

### Monitoring

<p align="center">
  <a href="docs/services/uptime-kuma.md"><img src="https://img.shields.io/badge/Uptime%20Kuma-Availability%20monitor-22C55E?style=for-the-badge&logo=uptimekuma&logoColor=white" alt="Uptime Kuma · Availability monitor"/></a>
  <a href="docs/services/netdata.md"><img src="https://img.shields.io/badge/Netdata-System%20metrics-00AB44?style=for-the-badge&logo=netdata&logoColor=white" alt="Netdata · System metrics"/></a>
</p>

## Technical documentation

| Subject | Detailed guide |
|---|---|
| Server specifications and limitations | [Hardware & system](docs/hardware.md) |
| Logical network design | [Network architecture](docs/network-architecture.md) |
| Network ports and access policy | [Network ports](docs/network-ports.md) |
| Access control, SSH, firewall and security improvements | [Security & hardening](docs/security.md) |
| Planned backup schedule and recovery testing | [Backup & recovery](docs/backup-recovery.md) |
| Infrastructure monitoring and metrics | [Monitoring](docs/monitoring.md) |
| Improvement milestones | [Roadmap](docs/roadmap.md) |
| Individual service pages | [All services](docs/services/README.md) |

## Next milestones

- [ ] Verify current OS version and the deployed service inventory
- [ ] Check accessible ports, Docker mappings and IPv6 exposure
- [ ] Add redacted screenshots and reproducible config examples
- [ ] Validate automatic backups and recovery tests
- [ ] Improve SSH authentication and internal HTTPS
- [ ] Plan an SSD upgrade for the HDD-based host

> **Security:** No VPN private keys, .env files, account credentials, backup archives or unredacted screenshots belong in this public repository.

---

<p align="center"><strong>Owen-Junior Jean</strong> · Network Engineering & Cybersecurity<br/><a href="https://github.com/lilouwen">GitHub</a> · <a href="https://www.linkedin.com/in/owen-junior-jean/">LinkedIn</a></p>
<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=95&section=footer" width="100%" alt="Footer"/></p>
