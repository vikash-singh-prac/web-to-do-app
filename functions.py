FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ To fetch the todos from the existing file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ TO write todos in the existing file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(__name__)

if __name__ == "__main__":
    print(get_todos())
    # print(write_todos(todos))
