# Homelab Xubuntu — Réseau, cloud et sécurité

Transformation d'un ancien PC portable ASUS en serveur personnel : DNS filtrant, VPN, cloud, coffre de mots de passe, partage de fichiers et supervision.

Ce projet permet de réutiliser du matériel existant tout en pratiquant l'administration Linux, Docker et la gestion d'un réseau domestique. L'accès distant passe par WireGuard ; les interfaces des applications restent destinées au réseau local et au VPN.



## Sommaire

- [Matériel et système](#matériel-et-système)
- [Architecture](#architecture)
- [Services installés](#services-installés)
- [Accès et ports locaux](#accès-et-ports-locaux)
- [Sécurité](#sécurité)
- [Sauvegardes](#sauvegardes)
- [Résultats et limites](#résultats-et-limites)
- [Roadmap](#roadmap)

## Matériel et système

| Élément | Configuration rapportée |
| --- | --- |
| Machine | PC portable ASUS |
| Processeur | 2 cœurs |
| Mémoire | 6 Go de RAM |
| Stockage | ~ 686 Go |
| Système | Xubuntu 26.04 LTS |
| Connexion | Ethernet |
| Adresse locale réservée | `192.168.1.187` |
| Routeur | Freebox — `192.168.1.254` |

Xubuntu conserve un environnement graphique pour l'administration sur place. L'administration courante s'effectue principalement à distance via SSH.

## Architecture

```text
                           INTERNET
                               |
                           [Freebox]
                         192.168.1.254
                               |
             +-----------------+------------------+
             |                                    |
       Reseau local                      Redirection UDP 51820
       PC / telephone                    Client distant WireGuard
             |                                    |
             +-----------------+------------------+
                               |
                    [Serveur Xubuntu ASUS]
                         192.168.1.187
                    VPN : 10.7.0.1/24
                               |
          +--------------------+--------------------+
          |                    |                    |
     Reseau / acces       Applications          Supervision
     - Pi-hole            - Homepage            - Uptime Kuma
     - WireGuard          - Nextcloud           - Netdata
     - SSH / Fail2ban        + MariaDB
     - Samba                + Redis
     - Syncthing          - Vaultwarden
                          - Portainer
```

Les services sont regroupés par fonction dans ce schéma. Ils ne dépendent pas tous les uns des autres : Portainer administre Docker, tandis qu'Uptime Kuma et Netdata assurent la supervision.

### Accès distant

```text
Telephone hors du domicile
          |
          | Tunnel WireGuard — UDP 51820
          v
       Freebox
          |
          v
Serveur VPN -> Services du homelab
```

Le compte rendu indique un test réussi depuis un téléphone en 4G/5G : échange WireGuard établi et trafic reçu/envoyé. Le téléphone utilise également Pi-hole lorsqu'il est connecté au VPN.

## Services installés

### Réseau et administration

| Service | Rôle dans le homelab |
| --- | --- |
| **Pi-hole** | DNS filtrant, blocage de domaines publicitaires et de suivi, statistiques et journalisation DNS. |
| **WireGuard** | Accès distant au réseau domestique à travers un tunnel VPN. |
| **SSH** | Administration du serveur depuis le PC principal. |
| **Fail2ban** | Protection notamment de SSH contre les tentatives répétées d'authentification ; décrit comme actif et activé au démarrage. |
| **Docker** | Exécution et isolation de plusieurs applications dans des conteneurs. |
| **Portainer** | Administration des conteneurs, images, volumes, réseaux et stacks Docker. |

Le PC principal utilise `192.168.1.187` comme DNS. Les clients WireGuard utilisent `10.7.0.1`. Le serveur VPN est décrit avec l'adresse `10.7.0.1/24` et le téléphone avec `10.7.0.2/24`.

### Applications et fichiers

| Service | Rôle dans le homelab |
| --- | --- |
| **Homepage** | Portail central regroupant les accès aux applications. |
| **Nextcloud** | Cloud personnel pour le stockage, la synchronisation et le partage de fichiers ; possibilité d'ajouter contacts et extensions. |
| **MariaDB** | Base de données de Nextcloud. |
| **Redis** | Service associé à Nextcloud. |
| **Vaultwarden** | Serveur de coffre de mots de passe compatible avec les clients Bitwarden. |
| **Samba** | Partage de fichiers accessible depuis l'Explorateur Windows. |
| **Syncthing** | Synchronisation directe de fichiers entre appareils, en complément de Nextcloud. |

Partage Windows :

```text
\\192.168.1.187\Partage
```

### Supervision

- **Uptime Kuma** suit la disponibilité, la latence et l'historique des services. Le compte rendu mentionne Pi-hole, Portainer, Vaultwarden, Netdata, Nextcloud, SSH et la Freebox parmi les éléments surveillés.
- **Netdata** permet de suivre CPU, RAM, swap, disque, entrées/sorties, réseau, processus et charge système. La surveillance du HDD est particulièrement utile sur cette machine.

### Conteneurs recensés

```text
homepage
nextcloud
nextcloud-db
nextcloud-redis
vaultwarden
uptime-kuma
portainer
```

Cette liste reprend les conteneurs explicitement cités dans le compte rendu ; elle ne suppose pas que tous les autres services utilisent Docker.

## Accès et ports locaux

Les adresses ci-dessous sont privées : elles s'utilisent depuis le LAN ou via le VPN, selon les règles d'accès configurées.

| Service | Port / protocole | Accès ou usage |
| --- | --- | --- |
| SSH | `22/TCP` | Administration sur `192.168.1.187` |
| Pi-hole — DNS | `53/UDP` et `53/TCP` | DNS local : `192.168.1.187` |
| Pi-hole — Web | `80/TCP` | [Administration Pi-hole](http://192.168.1.187/admin) |
| Homepage | `3000/TCP` | [Portail homelab](http://192.168.1.187:3000) |
| Uptime Kuma | `3001/TCP` | [Supervision des services](http://192.168.1.187:3001) |
| Vaultwarden | `8080/TCP` | [Coffre personnel](http://192.168.1.187:8080) |
| Nextcloud | `8081/TCP` | [Cloud personnel](http://192.168.1.187:8081) |
| Syncthing — Web | `8384/TCP` | Interface d'administration, selon l'adresse d'écoute configurée |
| Syncthing — synchronisation | `22000` | Port indiqué dans le compte rendu ; transports activés à vérifier |
| Portainer | `9443/TCP` | [Administration Docker](https://192.168.1.187:9443) |
| Netdata | `19999/TCP` | [Métriques système](http://192.168.1.187:19999) |
| WireGuard | `51820/UDP` | Point d'entrée VPN |
| Samba | `445/TCP` habituellement | Partage `\\192.168.1.187\Partage` ; ports effectifs à confirmer |

Les ports sont ceux du compte rendu ou déduits des URL indiquées. Le port Samba est donné comme repère usuel, sans vérification sur la machine. Les ports de MariaDB et Redis ne sont pas documentés comme publiés sur l'hôte.

## Sécurité

### Configuration décrite

- Une seule redirection entrante est prévue sur la Freebox : `51820/UDP` vers `192.168.1.187:51820` pour WireGuard.
- Les interfaces Web, SSH, le DNS et les partages de fichiers restent destinés au LAN et au VPN, sans exposition directe volontaire sur Internet.
- Fail2ban est actif pour protéger notamment SSH.
- L'administration de Vaultwarden utilise un secret stocké sous forme de hash Argon2id. Ni le secret ni son hash ne sont publiés ici.
- Le partage Samba décrit exige un utilisateur autorisé et désactive l'accès invité.

### Points à renforcer

- Passer SSH à une authentification par clés uniquement, après avoir validé l'accès par clé.
- Mettre en place HTTPS interne avec des certificats reconnus par les appareils, notamment pour Vaultwarden et Nextcloud. Les URL HTTP ci-dessus reflètent le compte rendu ; elles ne prouvent pas que tous les clients fonctionnent dans cette configuration.
- Vérifier les règles de pare-feu, les ports publiés par Docker et l'accès IPv6 pour confirmer le périmètre LAN/VPN souhaité.
- Maintenir le système et les applications à jour.

### Contenu destiné à GitHub

Ce dépôt documente l'installation. Les fichiers `.env`, mots de passe, jetons d'administration, clés privées, configurations WireGuard complètes, QR codes VPN, bases de données et archives de sauvegarde doivent rester hors du dépôt. Les sauvegardes WireGuard contiennent notamment des clés privées.

## Sauvegardes

### Plan quotidien prévu

Le compte rendu propose la planification suivante. L'exécution effective, le fuseau horaire des tâches et la restauration restent à valider sur le serveur.

| Horaire prévu | Élément | Source |
| --- | --- | --- |
| `03:00` | Vaultwarden | Volume Docker `vaultwarden_data` |
| `03:10` | WireGuard | Répertoire `/etc/wireguard` |
| `03:20` | Pi-hole | Répertoire `/etc/pihole` |
| `03:30` | Rotation | Suppression des archives de plus de 14 jours |

Organisation prévue :

```text
/home/oj/backups/
|-- vaultwarden/
|-- wireguard/
`-- pihole/
```

### Fiabilisation à prévoir

- Produire des sauvegardes cohérentes des bases de données, avec une méthode adaptée à chaque application ; une simple copie à chaud d'un volume peut être insuffisante.
- Ajouter Nextcloud, sa base MariaDB, ses données et sa configuration, ainsi que les fichiers importants du partage Samba.
- Conserver les définitions Docker Compose et les configurations utiles, en séparant les secrets de la documentation publique.
- Copier les archives sur un support externe ou un stockage hors site. Une sauvegarde sur le même HDD ne protège pas contre sa panne.
- Chiffrer les copies externes contenant des données sensibles et limiter les permissions d'accès.
- Tester régulièrement une restauration et surveiller les échecs de sauvegarde.

La synchronisation de fichiers avec Nextcloud ou Syncthing ne remplace pas une sauvegarde conservant des versions indépendantes.

## Résultats et limites

Le portable est réutilisé comme serveur DNS, VPN, cloud personnel, coffre de mots de passe, partage réseau, plateforme Docker et outil de supervision. Homepage centralise l'accès quotidien aux services.

Le HDD est identifié dans le compte rendu comme le principal facteur limitant, notamment pour Nextcloud et les bases de données. Un SSD constitue la priorité matérielle envisagée. Les 6 Go de RAM invitent également à surveiller l'utilisation mémoire avant d'ajouter de nouveaux services.

Tous les services reposent sur une seule machine et un seul disque : une panne peut interrompre l'ensemble du homelab. Aucune mesure chiffrée de consommation électrique ni aucun test de restauration n'est fourni dans le compte rendu.

## Roadmap

- [ ] Valider les sauvegardes quotidiennes, la rotation et une restauration complète.
- [ ] Mettre en place une copie externe ou hors site des sauvegardes.
- [ ] Étendre les sauvegardes à Nextcloud, MariaDB et aux fichiers partagés.
- [ ] Configurer l'authentification SSH par clés uniquement.
- [ ] Déployer HTTPS interne et un reverse proxy.
- [ ] Vérifier le filtrage réseau et les ports réellement accessibles.
- [ ] Activer les notifications Uptime Kuma.
- [ ] Remplacer le HDD par un SSD.
- [ ] Ajouter un tableau de bord WireGuard avancé.
- [ ] Évaluer Suricata IDS selon les ressources disponibles.
- [ ] Intégrer un appareil LILYGO comme console du homelab.
- [ ] Évaluer une suite bureautique intégrée à Nextcloud.


