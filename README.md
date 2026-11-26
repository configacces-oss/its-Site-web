# Informatique Team Services — site web

Site vitrine statique (HTML/CSS/JS, sans build), auto-hébergé sur NAS Synology via Docker + Cloudflare Tunnel.

- `site/` — les pages du site (`index.html`, `merci.html`, `mentions-legales.html`, `404.html`, images, robots/sitemap)
- `docker-compose.yml` — nginx (`its-site`) + Cloudflare Tunnel (`its-tunnel`)
- `docker/` — config nginx et script de démarrage (injecte `SITE_URL` depuis `.env`)
- `.env.example` — modèle de configuration (copier en `.env`, jamais commité)
- Formulaire de devis : FormSubmit (envoi par email, sans clé)

Installation pas à pas : voir [DEPLOIEMENT-NAS.md](DEPLOIEMENT-NAS.md).
