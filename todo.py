import os

def add_item(item):
  # Open the to-do list file in append mode
  with open("todo.txt", "a") as f:
    # Add the new item to the file
    f.write(item + "\n")

def mark_complete(item):
  # Read the current to-do list
  with open("todo.txt", "r") as f:
    items = f.readlines()

  # Overwrite the to-do list file with the updated list
  with open("todo.txt", "w") as f:
    for i in items:
      # If the item matches the item we want to mark as complete,
      # prefix it with a '[x]' to indicate it's done
      if i.strip() == item:
        f.write("[x] " + i)
      else:
        f.write(i)

def display_list():
  # Read the current to-do list
  with open("todo.txt", "r") as f:
    items = f.readlines()

  # Print the to-do list
  for i, item in enumerate(items):
    print(f"{i+1}. {item.strip()}")
