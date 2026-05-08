#!/bin/bash
# Exercise 3/3: Environment Script — HiveMind Pipeline Launcher
# Difficulty: Hard
# Concepts: export, variable guards, env variable patterns, bash scripting basics
#
# SCENARIO:
# HiveMind's inference pipeline requires three environment variables before
# it will run: HM_API_KEY, HM_MODEL, and HM_ENV. The team has been accidentally
# running experiments without these set, causing jobs to fail mid-run with
# cryptic errors. You've been asked to write a launcher script that:
#
#   1. Checks that all three required variables are set
#   2. Prints a clear error and exits if any are missing
#   3. Prints a confirmation summary if all are present
#   4. Simulates launching the pipeline (just echo the command for now)
#
# INSTRUCTIONS:
# 1. Set the three variables at the top of this script (use fake values)
# 2. Write the guard checks using [ -z "$VAR" ] pattern
# 3. Print a summary showing which model and environment will be used
# 4. Make this script executable: chmod +x 03_env_script.sh
# 5. Run it: ./03_env_script.sh
# 6. Then try commenting out one variable and running again — confirm the error
#
# YOUR SOLUTION:
# Write your script below this line.
# ─────────────────────────────────────

#!/bin/bash
# HiveMind Pipeline Launcher
# Usage: ./03_env_script.sh
# Requires: HM_API_KEY, HM_MODEL, HM_ENV to be exported in your shell

# --- Set variables (replace with: export VAR=value before running) ---
# Uncomment these to test the happy path:
# export HM_API_KEY="hm-key-abc123xyz"
# export HM_MODEL="llama-2-13b"
# export HM_ENV="staging"

# --- Guard checks ---
# Write your checks here.
# Pattern: if [ -z "$VARNAME" ]; then echo "ERROR: ..."; exit 1; fi



# --- Summary (only reached if all checks pass) ---
# Print something like:
# ✓ API key set (14 characters)
# ✓ Model: llama-2-13b
# ✓ Environment: staging
# Launching pipeline...



# HINT (uncomment to see the pattern for one check):
# if [ -z "$HM_API_KEY" ]; then
#     echo "ERROR: HM_API_KEY is not set."
#     echo "Run: export HM_API_KEY='your-key-here'"
#     exit 1
# fi

# EXPECTED OUTPUT (happy path):
# ✓ API key set (18 characters)
# ✓ Model: llama-2-13b
# ✓ Environment: staging
# Launching: python pipeline.py --model llama-2-13b --env staging

# EXPECTED OUTPUT (missing variable):
# ERROR: HM_API_KEY is not set.
# Run: export HM_API_KEY='your-key-here'
