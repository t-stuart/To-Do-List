import functions
import PySimpleGUI as gui

label = gui.Text("Create a To-Do List")
input_box = gui.InputText(tooltip="Enter a task")
add_button = gui.Button("Add")

window = gui.Window('My To-Do List', layout=[[label], [input_box, add_button]])
window.read()
window.close()
