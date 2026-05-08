#!/bin/bash
# Exercise 1/3: Variables and Export
# Difficulty: Easy
# Concepts: shell variables, export, checking inheritance
#
# SCENARIO:
# You're about to run a HiveMind training pipeline. The script expects
# two environment variables: MODEL_NAME and RUN_ID. Your job is to set
# them correctly and verify they're visible to child processes.
#
# INSTRUCTIONS:
# 1. Set a variable called MODEL_NAME with the value "llama-2-13b"
# 2. Set a variable called RUN_ID with the value "run-015"
# 3. Export both variables
# 4. Use bash -c to simulate a child process and echo both variables
# 5. Run: env | grep -E "MODEL_NAME|RUN_ID" to confirm they're in the environment
#
# YOUR SOLUTION:
# Write your commands below this line.
# ─────────────────────────────────────



# HINT (uncomment if stuck):
# export MODEL_NAME="llama-2-13b"
# export RUN_ID="run-015"
# bash -c 'echo "Running $MODEL_NAME as $RUN_ID"'
# env | grep -E "MODEL_NAME|RUN_ID"

# EXPECTED OUTPUT:
# Running llama-2-13b as run-015
# MODEL_NAME=llama-2-13b
# RUN_ID=run-015
