#from functions import get_todos , write_todos
import functions
import time
now = time.strftime("%b %d , %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Enter to add , show , edit , complete  ,exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif user_action.startswith('show'):

        todos = functions.get_todos()

        #new_todos = [item.strip('/n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("/n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo :")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt",todos)
        except ValueError:
            print("Your command is invalid")
            continue
    elif user_action.startswith('complete'):
        try:

            number = int(input("Enter the number of todo completed:"))

            todos = functions.get_todos()

            index = number - 1
            todo_removed = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"todo {todo_removed} was removed from the list"
            print(message)
        except ValueError:
            print("There is no item with that number")
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is invalid")
print('Bye')