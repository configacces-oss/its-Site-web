#!/bin/sh
# Copie le site et injecte l'URL et la clé Web3Forms définies dans .env
set -e
SITE_URL=$(printf '%s' "${SITE_URL:-http://localhost:8086}" | tr -d '\r' | sed 's:/*$::')
KEY=$(printf '%s' "${WEB3FORMS_KEY:-}" | tr -d '\r')
rm -rf /usr/share/nginx/html/*
cp -r /site/. /usr/share/nginx/html/
find /usr/share/nginx/html -type f \( -name '*.html' -o -name '*.xml' -o -name '*.txt' \) \
  -exec sed -i "s|__SITE_URL__|${SITE_URL}|g; s|__WEB3FORMS_KEY__|${KEY}|g" {} +
echo "Site ITS prêt : ${SITE_URL}"
exec /docker-entrypoint.sh nginx -g 'daemon off;'
