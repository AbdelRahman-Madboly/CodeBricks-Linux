#!/bin/bash
# Exercise 2/3: Command History
# Difficulty: Easy
# Concepts: history, ctrl+r, !!, !$
#
# SCENARIO:
# You ran several commands earlier while setting up a HiveMind experiment.
# Now you need to find and reuse them without retyping. This exercise is
# interactive — you'll do it in a live terminal, not by running this script.
#
# INSTRUCTIONS (run these in your terminal, not by executing this file):
#
# Step 1 — Run a few commands to build up history:
#   export MODEL_NAME="mistral-7b"
#   echo "Starting experiment with $MODEL_NAME"
#   ls ~/hivemind/logs/training/
#
# Step 2 — Use history to find them:
#   history | tail -10
#
# Step 3 — Use ctrl+r to search:
#   Press ctrl+r
#   Type "MODEL" — bash will show the most recent match
#   Press Enter to run it, or Esc to cancel
#
# Step 4 — Use !! and !$:
#   Run: echo ~/hivemind/logs/training/run-012.log
#   Then run: cat !$
#   (This runs: cat ~/hivemind/logs/training/run-012.log)
#
# Step 5 — Common real scenario:
#   Run any command without sudo (it will fail with "Permission denied")
#   Then run: sudo !!
#   (This repeats the last command with sudo prepended)
#
# ─────────────────────────────────────────────────────────────────────
# The commands below document what you should be able to do after this.
# Run them to see the output.

echo "=== History Practice Reference ==="
echo ""

# Show your 10 most recent commands
echo "--- Last 10 commands ---"
history | tail -10

echo ""
echo "--- Shortcuts to use interactively ---"
echo "ctrl+r    → reverse search (type to filter)"
echo "!!        → repeat last command"
echo "!$        → last argument of last command"
echo "!n        → run command number n from history"
echo "history -c → clear history (careful — irreversible)"

# EXPECTED RESULT:
# You can find a command from 10 minutes ago in under 3 seconds using ctrl+r.
