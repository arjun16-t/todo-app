import functions
import time

time_now = time.strftime("%A, %b %d, %Y %H:%M:%S %p")
print("It is:", time_now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    # if "add" in user_action:          -- earlier we used this but this just checked if add is anywhere in the string
    if user_action.startswith("add"):                   # this checks if user prompt starts with 'add'
        todo = user_action[4:].capitalize()
        with open("todo.txt", "a") as file:             # opening file to append new todos
            file.write(todo + "\n")

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):                # reading content from file to display
            print(f"{index+1}) {item.strip()}")

    elif user_action.startswith("edit"):
        try:                                                # try to run the code until ValueError
            num = int(user_action[5:])
            temp = input("What's new value? ")

            todos = functions.get_todos()

            print(f"{todos[num - 1].strip()}, is replaced by {temp}")
            todos[num - 1] = temp + '\n'

            functions.write_todos(todos)

        except ValueError:                                  # if there is a ValueError
            print("Please enter no. of todo to edit")       # gives user-friendly error
            continue                                        # and then re-runs the whole while block again

    elif user_action.startswith("complete"):
        try:
            rem = int(user_action[9:])
            todos = functions.get_todos()

            print(f"{todos[rem - 1].strip()} completed!")
            todos.pop(rem - 1)

            functions.write_todos(todos)

        except IndexError:
            print("There is no todo with that number! ")    # the try-except error keeps the prog running
            continue                                        # even after some error and re-runs the whole prog

    elif user_action.startswith("exit"):
        exit("bye!")
    else:
        print("Command is not valid")
