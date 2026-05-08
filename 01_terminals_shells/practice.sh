#!/bin/bash
# CH1: Terminals and Shells — Practice Script
# Run: bash practice.sh
# Read each section before running. Predict the output first.
# Some commands show what happens with and without export.

echo "=== CH1: Terminals and Shells ==="
echo ""

# ─── Section 1: Shell Variables ───────────────────────────────────────────────
echo "--- Shell Variables ---"

# Create a shell variable. No spaces around =.
# This variable only exists in the current shell session.
PROJECT="hivemind"
echo "Project: $PROJECT"
# Expected: Project: hivemind

# Double quotes: variables are expanded inside them
echo "Running on: $PROJECT server"
# Expected: Running on: hivemind server

# Single quotes: nothing is expanded — everything is literal
echo 'Running on: $PROJECT server'
# Expected: Running on: $PROJECT server

echo ""

# ─── Section 2: export ────────────────────────────────────────────────────────
echo "--- export ---"

# Without export: the variable is invisible to child processes
MODEL_NAME="llama-2-13b"
bash -c 'echo "Without export: $MODEL_NAME"'
# Expected: Without export:       (empty — bash subprocess can't see it)

# With export: child processes inherit the variable
export MODEL_NAME
bash -c 'echo "With export: $MODEL_NAME"'
# Expected: With export: llama-2-13b

# Create and export in a single step
export API_ENV="staging"
bash -c 'echo "Environment: $API_ENV"'
# Expected: Environment: staging

echo ""

# ─── Section 3: Checking variables ────────────────────────────────────────────
echo "--- Checking Variables ---"

# See all exported variables
echo "All env variables (first 5):"
env | head -5
# Expected: lines like HOME=/home/user, PATH=..., etc.

# Check a specific variable
echo "Current shell: $SHELL"
# Expected: /bin/bash (or similar)

echo "Home directory: $HOME"
# Expected: /home/<your-username>

echo ""

# ─── Section 4: History shortcuts ────────────────────────────────────────────
echo "--- History ---"

# Show recent history (interactive — works best in a live terminal)
echo "Recent commands (last 5):"
history | tail -5
# Expected: numbered list of your recent commands

# The ! shortcuts work interactively, not in scripts:
# !!    — repeat last command (e.g. sudo !!)
# !$    — last argument of last command (e.g. vim !$)
# ctrl+r — reverse search (press ctrl+r then start typing)
echo "(!! and ctrl+r only work in interactive terminals, not scripts)"

echo ""

# ─── Section 5: Practical pattern — env variable guard ───────────────────────
echo "--- Environment Variable Guard ---"

# This is the pattern you'll use in every real script:
# check that required variables are set before doing anything.

export FAKE_API_KEY="hm-key-abc123"

if [ -z "$FAKE_API_KEY" ]; then
    echo "ERROR: FAKE_API_KEY is not set. Export it before running."
    exit 1
else
    echo "API key found. Length: ${#FAKE_API_KEY} characters."
fi
# Expected: API key found. Length: 14 characters.

echo ""

# ─── Section 6: HiveMind connection ──────────────────────────────────────────
echo "--- HiveMind Example ---"

# HiveMind's warning.sh checks for a required env variable.
# This is the same pattern used before running ML pipelines.
echo "Run this to see the pattern in action:"
echo "  cat ~/hivemind/public/pipelines/warning.sh"
echo "  bash ~/hivemind/public/pipelines/warning.sh"
echo ""
echo "And the onboard script reads from stdin:"
echo "  bash ~/hivemind/public/pipelines/onboard.sh"

echo ""
echo "=== Done. Check your answers in notes.md ==="
