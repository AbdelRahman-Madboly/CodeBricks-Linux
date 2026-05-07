#!/bin/bash
# HiveMind AI — GPU Health Check
# Prints GPU memory usage across all production servers
# Usage: bash check_gpu.sh [--alert-threshold 80]

THRESHOLD=${2:-80}

echo "HiveMind GPU Health Check — $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================"

# In production this would SSH to each server and run nvidia-smi.
# For practice purposes, we simulate the output.

servers=("nietzsche" "kant" "spinoza" "descartes")
usage=(72 45 91 38)

for i in "${!servers[@]}"; do
    server="${servers[$i]}"
    pct="${usage[$i]}"
    if [ "$pct" -ge "$THRESHOLD" ]; then
        echo "WARNING  $server.hivemind-ai.com  GPU memory: ${pct}%  (above threshold)"
    else
        echo "OK       $server.hivemind-ai.com  GPU memory: ${pct}%"
    fi
done

echo "============================================"
echo "Threshold: ${THRESHOLD}%"
