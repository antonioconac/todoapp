from modules import functions
import FreeSimpleGUI as fs

label = fs.Text("Type in a to-do: ")
inputBox = fs.InputText(tooltip="Enter todo: ")
addButton = fs.Button("Add")

window = fs.Window("My to-do app GUI", layout=[[label], [inputBox, addButton]])
window.read()
window.close()