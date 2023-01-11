# Taskmaster-CLI
Taskmaster-CLI is a command-line tool for managing a to-do list. It has the following <br>features:
* Add an item to the to-do list
* Mark an item as complete
* Delete an item from the to-do list
* Clear the entire to-do list
* Display the current to-do list

This tool help user to maintain the To-do list and it could be used on day to day tasks as well as it could be used as a reminder.

## Requirements
Taskmaster-CLI requires Python 3 and Bash to be installed on your system.

## Installation
To install Taskmaster-CLI, clone the repository and navigate to the project directory:
```commandline
$ git clone https://github.com/jrzvnn/taskmaster-cli.git
$ cd taskmaster-cli
```
Make the todo.sh script executable:
`$ chmod +x todo.sh`

## Usage

To use Taskmaster-CLI, open a terminal and navigate to the project directory. Then, run the `todo.sh` script:
```commandline
$ ./todo.sh
```
You will be prompted to enter a command. The following commands are available:

* add item: Add a new item to the to-do list. Replace item with the text of the item you want to add.
* complete item: Mark an item as complete in the to-do list. Replace item with the text of the item you want to mark as complete.
* delete item: Delete an item from the to-do list. Replace item with the text of the item you want to delete.
* clear: Clear the entire to-do list.
* display: Display the current to-do list.

Here are some examples of using Taskmaster-CLI
```commandline
# Add an item to the to-do list
$ ./todo.sh
add Buy milk

# Mark an item as complete
$ ./todo.sh
complete Buy milk

# Display the current to-do list
$ ./todo.sh
display

```
