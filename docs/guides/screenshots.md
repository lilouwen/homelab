# Screenshot and public evidence policy

[← Documentation index](../README.md) · [← Repository](../../README.md)

The homelab is not currently available for new screenshots. Do not replace missing evidence with invented screenshots or images from another deployment.

## Candidate screenshots

| Service | Good evidence |
|---|---|
| Homepage | Sanitized overview of applications |
| Portainer | Container inventory and health, without credentials/identifying endpoints |
| Uptime Kuma | Availability summary with private hostnames removed |
| Netdata | CPU, memory, disk and network charts |
| Pi-hole | DNS service overview with client/query privacy protected |
| Nextcloud | Generic application screen without user files |
| WireGuard | Prefer topology and test summary rather than displaying peer settings |
| Vaultwarden | Avoid showing vault contents or admin token screens |

## Redaction checklist

- [ ] No public IP, domain, DNS query revealing browsing behavior or sensitive hostnames
- [ ] No passwords, tokens, cookies, environment variables or QR codes
- [ ] No SSH key or VPN peer private configuration
- [ ] No personally identifying file names or vault entries
- [ ] No authentication errors revealing usernames/accounts
- [ ] No personal notifications, open browser tabs or system username
- [ ] No original image metadata that should be private

**Use actual masking** before uploading; a blur alone may be reversible or incomplete. Review the final exported file.

## Storage

After validation, save images to `assets/screenshots/` and link them from the appropriate service page. Until then, keep the documentation text-only and honest about verification status.
