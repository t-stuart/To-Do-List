"""
While the functionality has been expanded,
the starter code is not original
and is only for educational purposes
"""


import functions
import PySimpleGUI as gui

label = gui.Text("Create a To-Do List")
input_box = gui.InputText(tooltip="Enter a task", key="task")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_list(), key="tasks",
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")

window = gui.Window('My To-Do List',
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_list()
            new_task = values["task"] + "\n"
            todo_list.append(new_task)
            functions.write_list(todo_list)
            window["tasks"].update(values=todo_list)
        case "Edit":
            task_to_edit = values["tasks"][0]
            new_task = values["task"]

            todo_list = functions.get_list()
            index = todo_list.index(task_to_edit)
            todo_list[index] = new_task
            functions.write_list(todo_list)
            window["tasks"].update(values=todo_list)
        case "tasks":
            window["task"].update(value=values["tasks"][0])

        case gui.WIN_CLOSED:
            break

window.close()
