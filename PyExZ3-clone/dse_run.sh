#!/bin/bash

# Ensure at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <python_file> [iterations]"
    exit 1
fi

# Set variables
export FILE_NAME="$1"
export INSTALL_PATH="$HOME/DSE/PyExZ3-clone/PyExZ3-clone"
export ITERATIONS="${2:-5}"  # Default to 1 iteration if not provided
TIME_LIMIT=30

# Resolve absolute file path
FILE_PATH=$(realpath "$FILE_NAME") || { echo "Error: Unable to resolve file path for $FILE_NAME"; exit 1; }
FILE_NAME=$(basename "$FILE_NAME" .py)

# Navigate to the DSE tool directory
cd "$INSTALL_PATH" || { echo "Error: DSE tool directory not found!"; exit 1; }

# Ensure Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Error: Python3 is not installed!"
    exit 1
fi

# Set up and activate the virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv || { echo "Failed to create virtual environment!"; exit 1; }
fi

echo "Activating virtual environment..."
source .venv/bin/activate || { echo "Failed to activate virtual environment!"; exit 1; }

# Ensure z3 is installed
if ! pip show z3 &>/dev/null; then
    echo "Installing z3..."
    pip install -q z3
else
    echo " z3 is already installed."
fi

# Determine entry point
if grep -qE '^def main\(' "$FILE_PATH"; then
    ENTRY_POINT="main"
elif grep -qE "^def ${FILE_NAME}\(" "$FILE_PATH"; then
    ENTRY_POINT="$FILE_NAME"
else
    ENTRY_POINT=""
fi

# Create results directory if not exists
mkdir -p ./Results/
OUTPUT_FILE="./Results/${FILE_NAME}_output.txt"

# Run DSE with correct parameters
echo "Running DSE tool on ${FILE_NAME}.py..."
if [ -n "$ENTRY_POINT" ]; then
    timeout "$TIME_LIMIT" python newpyexz3.py --start="$ENTRY_POINT" -m "$ITERATIONS" "$FILE_PATH" | tee "$OUTPUT_FILE"
else
    timeout "$TIME_LIMIT" python newpyexz3.py -m "$ITERATIONS" "$FILE_PATH" | tee "$OUTPUT_FILE"
fi


EXIT_STATUS=$?

if [ $EXIT_STATUS -eq 0 ]; then 
    echo "Dynamic symbolic execution completed succesfully. Output saved in '$OUTPUT_FILE'"

elif [ $EXIT_STATUS -eq 124 ]; then 
    echo "Exceution timed out after ${TIME_LIMIT} seconds" | tee -a "$OUTPUT_FILE"
    exit 1
else
    echo "Error: DSE test failed with exit code $EXIT_STATUS!" | tee -a "$OUTPUT_FILE"
    exit $EXIT_STATUS
fi


# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate || { echo "Failed to deactivate virtual environment!"; exit 1; }

