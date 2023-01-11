#!/usr/bin/env bash

# This bash script serves as the entry point for the to-do list tool.
# It handles user input and invokes the appropriate functions in the Python script.

# The path to the Python script
SCRIPT_PATH='./todo.py'

# Read a single line of input from the user
read -r INPUT 

# Split the input into an array of words
WORDS=($INPUT)

# The first word is the command
COMMAND=${WORDS[0]}

# The rest of the words are the arguments
ARGS=${WORDS[@]:1}

# Invoke the appropriate function in the python script
if [ "${COMMAND}" == 'add' ]; then
    python3 "$SCRIPT_PATH" add "$ARGS"
elif [ "${COMMAND}" == 'complete' ]; then
    python3 "$SCRIPT_PATH" complete "$ARGS"
elif [ "${COMMAND}" == 'delete' ]; then
    python3 "$SCRIPT_PATH" delete "$ARGS"
elif [ "${COMMAND}" == 'clear' ]; then
    python3 "$SCRIPT_PATH" clear 
elif [ "${COMMAND}" == 'display' ]; then
    python3 "$SCRIPT_PATH" display 
else
  echo "Unrecognized command: $COMMAND"
fi  