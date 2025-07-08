from modules import functions
import FreeSimpleGUI as fs
import time

now = time.strftime('%b %d, %Y, %H:%M:%S')
fs.theme("Black")

clock = fs.Text('', key = 'clock')
label = fs.Text("Type in a to-do: ")
inputBox = fs.InputText(tooltip="Enter todo: ", key= "todo")
addButton = fs.Button("Add", size=10)
listBox = fs.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45, 10])
editButton = fs.Button("Edit")
completeButton = fs.Button("Complete")
exitButton = fs.Button("Exit")

window = fs.Window("My to-do app GUI",
                   layout=[[clock],
                           [label],
                           [inputBox, addButton],
                           [listBox, editButton, completeButton],
                           [exitButton]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
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
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fs.popup('Please select an item first.')
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fs.popup('Please select an item first.')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fs.WIN_CLOSED:
            break

window.close()