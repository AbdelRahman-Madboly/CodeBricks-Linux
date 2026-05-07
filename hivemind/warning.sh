#!/bin/sh

# HiveMind AI — warning broadcast script
# Usage: WARN_MESSAGE="disk full" WARN_FROM_NAME="Priya" ./warning.sh

echo "============================================"
echo "=========== HIVEMIND AI WARNING ============"
echo "============================================"
echo "$WARN_MESSAGE"
echo "============================================"
echo "From: $WARN_FROM_NAME"
echo "============================================"

if [ -z "$WARN_MESSAGE" ]; then
    echo "WARN_MESSAGE is not set. Exiting with error."
    exit 1
fi

if [ -z "$WARN_FROM_NAME" ]; then
    echo "WARN_FROM_NAME is not set. Exiting with error."
    exit 1
fi
