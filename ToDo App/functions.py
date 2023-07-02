def get_list(filepath="todo_list.txt"):
    """ Read a text file and return the list of tasks """
    with open(filepath) as local_file:
        text_file = local_file.readlines()
    return text_file


def write_list(tasks, filepath="todo_list.txt"):
    """ Writes a text file with a task list as the contents """
    with open(filepath, "w") as local_file:
        local_file.writelines(tasks)