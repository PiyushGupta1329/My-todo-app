import functions
import time

# it is used to show time in our project
#to show date and time we use pythin format codes

now = time.strftime("%b %d, %Y %H:%M:%S")#month day year time
print("It is", now)



while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos#function call

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            functions.write_todos(todos)

            new_todo = input("enter new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("command is not valid")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])


            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that no.")
            continue

    elif user_action.startswith('exit'):
        print("bye AMIGO!!")
        break
    else:
        print("command is not valid")


#write function only with read mode only
#repetive code in read and write file modes also