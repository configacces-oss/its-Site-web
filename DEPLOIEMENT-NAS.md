# Héberger le site ITS sur un NAS Synology (Cloudflare Tunnel)

Architecture : **Internet → Cloudflare (HTTPS) → tunnel chiffré → NAS (Container Manager) → nginx**
Aucun port à ouvrir sur la box, IP du NAS jamais exposée, certificat HTTPS automatique.

## Prérequis
- DSM 7.2+ avec **Container Manager** installé (Centre de paquets)
- Un nom de domaine (ex. `itservices75.fr`) dont les DNS sont gérés par **Cloudflare** (compte gratuit)
- Une clé **Web3Forms** (gratuite) pour recevoir les demandes de devis par email

## 1. Clé Web3Forms (2 min)
1. Aller sur https://web3forms.com → « Create your Access Key »
2. Saisir l'email qui doit **recevoir** les demandes (ex. `assistance@itservices75.fr`)
3. Copier la clé reçue par email

## 2. Domaine sur Cloudflare (si pas déjà fait)
1. https://dash.cloudflare.com → **Add a domain** → `itservices75.fr` → plan Free
2. Vérifier que les enregistrements **MX** (emails) ont bien été importés — sinon les recopier depuis le registrar actuel **avant** de changer les DNS
3. Chez le registrar (OVH, Gandi, IONOS…), remplacer les serveurs DNS par les 2 indiqués par Cloudflare

## 3. Créer le tunnel
1. Cloudflare → **Zero Trust** → **Networks** → **Tunnels** → **Create a tunnel** → type **Cloudflared**
2. Nom : `its-nas` → Save
3. Choisir l'environnement **Docker** et copier **uniquement le jeton** (la longue chaîne après `--token`)
4. Onglet **Public Hostname** → **Add a public hostname** :
   | Champ | Valeur |
   |---|---|
   | Subdomain | `www` |
   | Domain | `itservices75.fr` |
   | Service Type | `HTTP` |
   | URL | `site:80` |
5. Répéter avec Subdomain vide (domaine nu) si vous voulez que `itservices75.fr` fonctionne aussi

## 4. Copier les fichiers sur le NAS
Dans **File Station**, créer le dossier `docker/its-site` et y déposer :
```
its-site/
├── docker-compose.yml
├── .env               ← à créer depuis .env.example
├── docker/
│   ├── nginx.conf
│   └── start.sh
└── site/
    └── (index.html, images, etc.)
```
Créer `.env` (copie de `.env.example`) et remplir :
```
SITE_URL=https://www.itservices75.fr
WEB3FORMS_KEY=votre-cle-web3forms
CLOUDFLARE_TUNNEL_TOKEN=votre-jeton-cloudflare
```

## 5. Lancer dans Container Manager
1. **Container Manager** → **Projet** → **Créer**
2. Nom : `its-site` — Chemin : `/docker/its-site` — Source : **Utiliser le docker-compose.yml existant**
3. Suivant → Terminé : les conteneurs `its-site` et `its-tunnel` démarrent

Vérifications :
- En local : `http://IP-DU-NAS:8086`
- Dans Cloudflare → Tunnels : le tunnel `its-nas` doit être **HEALTHY**
- En public : `https://www.itservices75.fr`
- Envoyer un devis test depuis le site → l'email doit arriver

## Mettre à jour le site
Remplacer les fichiers du dossier `site/` dans File Station, puis Container Manager → Projet `its-site` → **Action → Redémarrer**.

## Réglages Cloudflare conseillés
- SSL/TLS → mode **Full** (ou Flexible si erreur)
- SSL/TLS → Edge Certificates → **Always Use HTTPS** : activé
- Rules → Redirect Rules : rediriger `itservices75.fr` vers `www.itservices75.fr`

## Dépannage
| Symptôme | Cause probable |
|---|---|
| Tunnel « DOWN » | Jeton mal copié dans `.env` (espaces, retour à la ligne) |
| Erreur 502 | URL du Public Hostname différente de `site:80` |
| Formulaire « Envoi impossible » | `WEB3FORMS_KEY` vide ou erronée → corriger `.env` puis redémarrer |
| Port 8086 déjà utilisé | Changer `8086:80` dans `docker-compose.yml` (ou supprimer la ligne, le tunnel n'en a pas besoin) |
