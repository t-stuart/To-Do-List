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

window = gui.Window('My To-Do List',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 12))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todo_list = functions.get_list()
            new_task = value["task"]
            todo_list.append(new_task)
            functions.write_list(todo_list)
        case gui.WIN_CLOSED:
            break

window.close()

