#!/bin/bash
set -euo pipefail

SOURCE="${1:-}"
DEST="${2:-$HOME/backups}"
KEEP=5

if [ -z "$SOURCE" ]; then
    echo "Usege: $0 <source_dir> [backup_dir]" >&2
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "Error: '$SOURCE' is not directory" >&2
    exit 2
fi

mkdir -p "$DEST"
LOG_FILE="$DEST/backup.log"

log() {
    echo "$(date '+%F %T') $1" | tee -a "$LOG_FILE"
}

TIMESTAMP=$(date +%F_%H-%M-%S)
NAME=$(basename "$SOURCE")
ARCHIVE="$DEST/${NAME}_${TIMESTAMP}.tar.gz"

trap 'rm -f "$ARCHIVE"; log "ERROR: backup failed, partial archive removed"' ERR

log "Starting backup of $SOURCE"
tar -czf "ARCHIVE" "$SOURCE"
trap - ERR
log "Created $ARCHIVE"

ls -1t "$DEST/${NAME}_"*.tar.gz | tail -n +$((KEEP + 1)) | xargs -r rm ---
log "Rotation done, keeping last $KEEP archives"
