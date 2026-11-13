# Docker

[← Service directory](README.md) · [Repository home](../../README.md)

**Category:** Containers & applications  
**Function:** Container runtime  
**Reported access / ports:** Depends on container mappings

## Purpose

Run the documented self-hosted containers.

## Documented project notes

Docker is used to deploy and manage multiple self-hosted applications.

Portainer provides a web-based management interface for containers, images, networks, volumes and stacks.

## Containerized Services

| Container | Description |
|---|---|
| `homepage` | Central dashboard for homelab applications |
| `nextcloud` | Private cloud and file collaboration |
| `nextcloud-db` | MariaDB database for Nextcloud |
| `nextcloud-redis` | Redis service associated with Nextcloud |
| `vaultwarden` | Self-hosted password manager |
| `uptime-kuma` | Service availability monitoring |
| `portainer` | Docker management interface |

These containers were identified in the deployment documentation. Their current runtime state should be verified on the server.

## Homepage

Homepage acts as the central entry point for the homelab.

It provides organized access to self-hosted applications and infrastructure management tools.

## Nextcloud

Nextcloud provides personal cloud storage and file management.

The documented deployment includes:

- Nextcloud application.
- MariaDB database.
- Redis service.

Future improvements may include additional collaboration features and more robust backup procedures.

## Vaultwarden

Vaultwarden provides a self-hosted password management service compatible with Bitwarden clients.

The documented configuration uses an Argon2id-hashed administration secret.

The secret and its hash must remain outside this public repository.

## Portainer

Portainer provides centralized Docker management.

Main functions include:

- Container inspection.
- Image management.
- Docker volume administration.
- Docker networking.
- Stack deployment and maintenance.

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
