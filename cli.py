from modules import functions
import time

now = time.strftime("%b %d, %Y, %H:%M:S")
print("It is: " + now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item.title()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            new_todo = input("Enter a new to do: ")
            todos[number - 1] = new_todo + '\n'
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            removed_todo = todos[index].strip("\n")
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {removed_todo} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that index.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")

print("Bye!")