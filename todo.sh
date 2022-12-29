#!/usr/bin/env bash

# Display the current to-do list
python todo.py display

echo "Enter a command (add, complete, display):"

# Read a single line of input from the user
# shellcheck disable=SC2162
read command

case $command in
  # If the user entered "add", ask for the item to add
  add)
    echo "Enter the item to add:"
    # shellcheck disable=SC2162
    read item
    python todo.py add "$item"
    ;;

  # If the user entered "complete", ask for the item to mark as complete
  complete)
    echo "Enter the item to mark as complete:"
    # shellcheck disable=SC2162
    read item
    python todo.py complete "$item"
    ;;

  # If the user entered "display", display the current to-do list
  display)
    python todo.py display
    ;;

  # If the user entered an invalid command, display an error message
  *)
    echo "Invalid command"
    ;;
esac
