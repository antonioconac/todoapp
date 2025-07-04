from modules import functions
import FreeSimpleGUI as fs

label = fs.Text("Type in a to-do: ")
inputBox = fs.InputText(tooltip="Enter todo: ", key= "todo")
addButton = fs.Button("Add")
listBox = fs.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
editButton = fs.Button("Edit")

window = fs.Window("My to-do app GUI",
                   layout=[[label], [inputBox, addButton], [listBox, editButton]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fs.WIN_CLOSED:
            break

window.close()