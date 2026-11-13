# Network architecture

## Network Architecture

The infrastructure is built around a Freebox router and a Linux server hosting multiple networking, security and application services.

## Logical Network Topology

```mermaid
flowchart TB

    REMOTE["Remote Client<br/>4G / 5G"]
    INTERNET["Internet"]
    ROUTER["Freebox Router<br/>192.168.1.254"]
    LAN["Local Network<br/>PC / Mobile Devices"]

    REMOTE --> INTERNET
    INTERNET --> ROUTER
    LAN --> ROUTER

    subgraph SERVER["ASUS HOMELAB — XUBUNTU LINUX"]
        direction TB

        subgraph NETWORK["NETWORKING & SECURITY"]
            WG["WireGuard VPN"]
            DNS["Pi-hole DNS"]
            SSH["SSH + Fail2ban"]
            SAMBA["Samba"]
            SYNC["Syncthing"]
        end

        subgraph DOCKER["DOCKER ENVIRONMENT"]
            PORT["Portainer"]
            HOME["Homepage"]
            VAULT["Vaultwarden"]
            CLOUD["Nextcloud"]
            DB["MariaDB"]
            CACHE["Redis"]
            KUMA["Uptime Kuma"]
        end

        subgraph OBSERVABILITY["SYSTEM MONITORING"]
            NETDATA["Netdata"]
        end

        CLOUD --> DB
        CLOUD --> CACHE
    end

    ROUTER -->|"Ethernet / LAN"| SSH
    ROUTER -->|"UDP 51820"| WG

    LAN -.->|"DNS Requests"| DNS
    WG -.->|"VPN DNS"| DNS
    WG -.->|"Private Access"| HOME

    PORT -.->|"Container Management"| CLOUD
    KUMA -.->|"Service Monitoring"| CLOUD
    NETDATA -.->|"Host Metrics"| SSH

    classDef external fill:#17213a,stroke:#64748b,color:#ffffff
    classDef security fill:#302b63,stroke:#818cf8,color:#ffffff
    classDef service fill:#153b57,stroke:#38bdf8,color:#ffffff

    class REMOTE,INTERNET,ROUTER,LAN external
    class WG,DNS,SSH,SAMBA,SYNC security
    class PORT,HOME,VAULT,CLOUD,DB,CACHE,KUMA,NETDATA service
```

### Architecture Explanation

The Freebox acts as the main gateway between the home network and the Internet.

The ASUS laptop hosts the Linux infrastructure and its associated services.

The architecture is organized into three functional areas:

**Networking & Security**

- Private network connectivity.
- DNS filtering.
- VPN access.
- SSH administration.
- File sharing and synchronization.
- Authentication protection.

**Containerized Applications**

- Private cloud storage.
- Password management.
- Service dashboard.
- Container administration.
- Availability monitoring.

**System Monitoring**

- Resource utilization.
- Service availability.
- Storage performance.
- Network activity.

The diagram represents a logical grouping of services, not necessarily their exact deployment method or network isolation.

---

[← Repository home](../README.md) · [Service directory](services/README.md)
