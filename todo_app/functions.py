DATAFILE='todos.txt'

def get_todos(datafile=DATAFILE):
    """Reads a text file and return a list of todo items."""
    with open(datafile, 'r') as file:
            todos = file.readlines()
    return todos
   
def write_todos(var_local, datafile=DATAFILE):
    """Writes the user input as a new todo to the text file.""" 
    with open(datafile, 'w') as file:
            file.writelines(var_local)