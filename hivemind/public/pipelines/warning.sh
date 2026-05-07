#!/bin/sh

# This script prints branded HiveMind warning messages.
# Set WARN_MESSAGE and WARN_FROM before running.
#
# Usage:
#   WARN_MESSAGE="GPU memory critical" WARN_FROM="monitoring" bash warning.sh

echo "============================================"
echo "=========== HIVEMIND AI WARNING ============"
echo "============================================"
echo "$WARN_MESSAGE"
echo "============================================"
echo "From: $WARN_FROM"
echo "============================================"

if [ -z "$WARN_MESSAGE" ]; then
    echo "Error: WARN_MESSAGE is not set."
    exit 1
fi

if [ -z "$WARN_FROM" ]; then
    echo "Error: WARN_FROM is not set."
    exit 1
fi
