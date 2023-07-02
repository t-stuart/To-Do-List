"""
While the functionality has been expanded,
the starter code is not original
and is only for educational purposes
"""
from functions import get_list, write_list
import time

date = time.strftime("%B %d, %Y")
day = time.strftime("%A")
current_time = time.strftime("%I:%M%p")
print(f"{day} {date}, {current_time}")

while True:
    # Get user input and make case-insensitive
    user_action = input("Please type a command (add, show, edit, complete or exit)")
    user_action = user_action.lower()

    if user_action.startswith('add'):
        task = user_action[4:]

        todo_list = get_list()

        todo_list.append(task + "\n")

        write_list(todo_list)

    elif user_action.startswith('show'):
        with open(r"todo_list.txt") as file:
            todo_list = file.readlines()

        # alternate to 'for loop' below
        # new_todo_list = [item.strip('\n') for item in item_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            list_num = int(user_action[5:]) - 1

            todo_list = get_list()

            todo_list[list_num] = input('Enter the new task: ') + "\n"

            write_list(todo_list)

        except ValueError:
            print("Sorry, that is not a valid command.")
            continue

    elif user_action.startswith('complete'):
        try:
            finished_item_index = int(user_action[9:]) - 1

            todo_list = get_list()

            completed_task = todo_list[finished_item_index].strip('\n')
            todo_list.pop(finished_item_index)

            write_list(todo_list)

            message = f"{completed_task} was removed from the list"
            print(message)

        except IndexError:
            print("That task number does not exist.")

    elif user_action.startswith('exit'):
        break

    else:
        print("Sorry, that is not a valid command.")

print("See you later!")
