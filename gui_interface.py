"""
While the functionality has been expanded,
the starter code is not original
and is only for educational purposes
"""


import functions
import PySimpleGUI as gui
import time

gui.theme('DarkBlue12')

clock = gui.Text('', key='clock')
label = gui.Text("Create a To-Do List")
input_box = gui.InputText(tooltip="Enter a task", key="task")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_list(), key="tasks",
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window('My To-Do List',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%A %B %d, %Y %I:%M:%S"))
    match event:
        case "Add":
            todo_list = functions.get_list()
            new_task = values["task"] + "\n"
            todo_list.append(new_task)
            functions.write_list(todo_list)
            window["tasks"].update(values=todo_list)
            window["task"].update(value='')
        case "Edit":
            try:
                task_to_edit = values["tasks"][0]
                new_task = values["task"]

                todo_list = functions.get_list()
                index = todo_list.index(task_to_edit)
                todo_list[index] = new_task
                functions.write_list(todo_list)
                window["tasks"].update(values=todo_list)
            except IndexError:
                gui.popup("Please select the task you want to edit", font=("Helvetica", 10))
        case "Complete":
            try:
                task_to_complete = values["tasks"][0]
                todo_list = functions.get_list()
                todo_list.remove(task_to_complete)
                functions.write_list(todo_list)
                window["tasks"].update(values=todo_list)
                window["task"].update(value='')
            except IndexError:
                gui.popup("Please select the task you want to complete", font=("Helvetica", 10))
        case "Exit":
            break
        case "tasks":
            window["task"].update(value=values["tasks"][0])

        case gui.WIN_CLOSED:
            break

window.close()
