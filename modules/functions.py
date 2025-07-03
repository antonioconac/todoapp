FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a .txt file and return the content of the file as a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath=FILEPATH):
    """Write the content of a list inside a .txt file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_list)
