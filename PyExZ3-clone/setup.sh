#!/bin/bash

# Homebrew default locations (both for python and z3)
export PYTHONMODS="/usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/local/bin/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz"
export Z3HOME="/home/nikhilesh-matta/z3/build/python"
export Z3BIN="/home/nikhilesh-matta/z3/Z3HOME/bin"


# Python setup
export PYTHONPATH=$PYTHONMODS:$Z3HOME

# Path setup
export PATH=$PATH:$Z3BIN


