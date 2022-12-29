#!/usr/bin/env python

"""
 This Python script stores and retrieves to-do list items from a text file.
 It has functions for adding a new item, marking an item as completed, deleting
 an item, clearing the to-do list, and displaying the current to-do list.
"""

import sys


# The path to the to-do list text file
TODO_FILE = 'todo.txt'


def add_item(item):
    """Add a new item to the to-do list."""
    with open(TODO_FILE, 'a') as f:
        f.write(item + '\n')
    

def mark_complete(item):
    """Mark an item as complete in the to-do list."""
    items = []
    with open(TODO_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line == item:
                items.append('[x] ' + line)
            else:
                items.append(line)
    with open(TODO_FILE, 'w') as f:
        for item in items:
            f.write(item + '\n')


def delete_item(item):
  """Delete an item from the to-do list."""
  items = []
  with open(TODO_FILE, 'r') as f:
    for line in f:
      line = line.strip()
      if line != item:
        items.append(line)
  with open(TODO_FILE, 'w') as f:
    for item in items:
      f.write(item + '\n')

def clear_list():
    """Clear the to-do list"""
    with open(TODO_FILE, 'w') as f:
        f.write('')


def display_list():
    """Display the current to-do list"""
    with open(TODO_FILE, 'r') as f:
        for line in f:
            print(line.strip())


def main():
    """Handle command-line arguments and invoke the appropriate function."""
    if len(sys.argv) < 2:
        print('Usage: python todo.py [add|complete|delete|clear|display] ITEM')
        sys.exit(1)
    
    command = sys.argv[1]
    if command == 'add':
        if len(sys.argv) != 3:
            print('UsageL python todo.py add ITEM')
            sys.exit(1)
        item = sys.argv[2]
        add_item(item)
    elif command == 'complete':
        if len(sys.argv) != 3:
            print('Usage: python todo.py complete ITEM')
            sys.exit(1)
        item = sys.argv[2]
        mark_complete(item)
    elif command == 'delete':
        if len(sys.argv) != 3:
            print('Usage: python todo.py delete ITEM')
            sys.exit(1)
        item = sys.argv[2]
        delete_item(item)
    elif command == 'clear':
        clear_list()
    elif command == 'display':
        display_list()
    else:
        print(f"Unrecognized command: {command}")


if __name__ == '__main__':
    main()
