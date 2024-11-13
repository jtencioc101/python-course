import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

# Actions
add_todo = sg.Text("Type in a to-do")

# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# App body
sg.theme("DarkPurple4")
clock = sg.Text('', key='clock')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
window = sg.Window('My Todo App',
                   layout = [[clock],
                            [add_todo], [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font = ('Helvetica', 20))
            
# App Logic
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))          
        case "todos":
            window['todo'].update(value=values['todos'][0])        
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                   sg.popup("Please select an item first", font=("Helvetica", 20)) 
        case "Exit":
            break        
        case sg.WIN_CLOSED:
            break
    
window.close()
