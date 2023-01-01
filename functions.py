from constants import BASEFILE

def get_todos(filepath=BASEFILE):
    """
    Read a text file and return a list of todos
    :param filepath: the path of the to-be-read file
    :return: a list of lines read from the file that 'filepath' points to
    """
    with open(filepath, 'r') as file_local:
        return file_local.readlines()


def write_todos(todos_local, filepath=BASEFILE):
    """
    Write a list of todos to a specified text file
    :param todos_local: a list of todos to be written to a file
    :param filepath: the path to the to-be-written file
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


"""
    __name__ stores:
    1. the name of the file, or
    2. "__main__" if the script/file that is being run directly
"""


if __name__ == "__main__":
    print("Hello!")