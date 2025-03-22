#!/bin/bash

# Ensure correct usage
if [ $# -lt 1 ]; then
    echo "Usage: $0 <python_file> <iterations>"
    exit 1
fi

export BENCHMARK=$1
ITERATIONS=${2:-1}  # Take iterations count from user input

# Move to PyExZ3 directory
cd PyExZ3-clone || { echo "Error: PyExZ3-clone directory not found."; exit 1; }

# Get the filename without extension
BENCHMARK=$(basename "$BENCHMARK" .py)

if [ -z "$BENCHMARK" ]; then
    echo "Error: Please provide a Python file for testing."
    exit 1
fi

FileName=$1

# Check if the file exists
if [ ! -f "$FileName" ]; then
    echo "Error: File '$FileName' not found."
    exit 1
fi

# Check if 'main' function exists in the file
if grep -qE '^def main\(' "$FileName"; then
    ENTRY_POINT="main"
elif grep -qE "^def ${BENCHMARK}\(" "$FileName"; then
    ENTRY_POINT="$BENCHMARK"
else
    ENTRY_POINT=""
fi

# Run PyExZ3 and store output in a variable
if [ -n "$ENTRY_POINT" ]; then
    OUTPUT=$(python newpyexz3.py --start="$ENTRY_POINT" -m "$ITERATIONS" "$FileName")
else
    OUTPUT=$(python newpyexz3.py -m "$ITERATIONS" "$FileName")
fi

# Print output
echo "$OUTPUT"

