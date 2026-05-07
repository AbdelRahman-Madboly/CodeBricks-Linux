#!/bin/sh

echo "Welcome to the HiveMind AI onboarding CLI!"
echo ""
echo "Please enter your name:"
read NAME

echo "Please enter your role (engineer/researcher/ops):"
read ROLE

echo "Please enter your preferred GPU (a100/h100/rtx4090/cpu-only):"
read GPU

echo "============================================"
echo "Welcome, $NAME!"
echo "Role   : $ROLE"
echo "GPU    : $GPU"
echo "============================================"
echo "Your onboarding request has been logged."
echo "Tomás from DevOps will set up your access within 1-3 business days."
echo "Or immediately, if you bring him coffee."
echo "Goodbye!"
