from modules import functions
import FreeSimpleGUI as fs

label = fs.Text("Type in a to-do: ")
inputBox = fs.InputText(tooltip="Enter todo: ", key= "todo")
addButton = fs.Button("Add")

window = fs.Window("My to-do app GUI", layout=[[label], [inputBox, addButton]], font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_value = values['todo'] + "\n"
            todos.append(new_value)
            functions.write_todos(todos)
        case fs.WIN_CLOSED:
            break

window.close()