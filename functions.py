FILEPATH = "todos.txt"          # CONSTANT VARIABLE


def get_todos(filepath=FILEPATH):
    """ Reads the file and returns the list of todos items """
    with open(filepath, "r") as file_local:
        get_todo = file_local.readlines()
    return get_todo


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items in list of text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from func")
    print(get_todos())