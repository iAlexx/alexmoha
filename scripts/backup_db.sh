#!/usr/bin/env sh
set -eu

BACKUP_DIR=${BACKUP_DIR:-/backups}
TS=$(date +%Y%m%d_%H%M%S)
OUT="$BACKUP_DIR/finintel_$TS.sql"

mkdir -p "$BACKUP_DIR"
export PGPASSWORD="${POSTGRES_PASSWORD:-postgres}"
pg_dump -h "${POSTGRES_HOST:-postgres}" -U "${POSTGRES_USER:-postgres}" "${POSTGRES_DB:-finintel}" > "$OUT"

echo "Backup created: $OUT"
