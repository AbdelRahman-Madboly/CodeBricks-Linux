#!/bin/bash
# HiveMind AI — Model Backup Script
# Backs up all checkpoint files to /backup/
# Run as: bash backup.sh
# Scheduled via cron: 0 2 * * * /hivemind/scripts/backup.sh

BACKUP_DIR="/backup/hivemind/$(date +%Y-%m-%d)"
SOURCE_DIR="/hivemind/private/models/checkpoints"
LOG_FILE="/hivemind/logs/system/backup.log"

echo "$(date '+%Y-%m-%d %H:%M:%S') INFO  Backup started" >> $LOG_FILE

# BUG: this will fail silently if BACKUP_DIR already exists
mkdir $BACKUP_DIR

cp -r $SOURCE_DIR $BACKUP_DIR

# BUG: no check that cp succeeded before logging success
echo "$(date '+%Y-%m-%d %H:%M:%S') INFO  Backup complete: $BACKUP_DIR" >> $LOG_FILE

echo "Done."
