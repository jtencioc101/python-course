#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d %Y, %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action.replace("add ","", 1) + "\n"
        todos = functions.get_todos()      
        todos.append(todo)                 
        functions.write_todos(todos)  
        
    elif user_action.startswith("show"): 
        todos = functions.get_todos()          
        for index, item in enumerate(todos):  
            data = f"{index + 1}-{item.capitalize()}"
            print(data.strip())
    
    elif user_action.startswith("edit"):  
        try:           
            number = int(user_action[5:])
            number = number -1
            todos = functions.get_todos()
            print("Now editing: ",todos[number].capitalize())
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo  + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your Command is not valid")
            continue
            
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[8:])
            todos = functions.get_todos()
            completed_task = todos.pop(number -1).strip()
            functions.write_todos(todos) 
            print(f"{completed_task.capitalize()} has been completed!")
        except IndexError:
            print("There is no task with that number, please try again.")
            continue
        
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command, please type add, show or exit: ")
print("Bye!")