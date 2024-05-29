

def read_todos(filename):
    todos_file = open(filename, "r")
    file_contents = todos_file.read()
    todos = file_contents.split("\n")
    todos_file.close()
    todos_in_parts = []
    for todo in todos:
        todo_parts = todo.split(",")
        if len(todo_parts) > 1:
            todo_dict = {
                "done" : todo_parts[2],
                "todo_text" : todo_parts[1],
                "todo_id" : todo_parts[0]
            }
            todos_in_parts.append(todo_dict)
    return todos_in_parts

def view_incomplete_todos():
    todos = read_todos('todos.csv')
    for todo in todos:
        ## check to see if it's not done, if so:
        if todo["done"] == "0":
            print(todo["todo_id"] + ": " + todo["todo_text"])

def complete_todo(completed_todo_id):
    todos = read_todos('todos.csv')
    todos_file = open('todos.csv', 'w')
    for todo in todos:        
        done = todo["done"]
        todo_text = todo["todo_text"]
        todo_id = todo["todo_id"]
        todo_parts = [todo_id,todo_text,done]
        if completed_todo_id == todo_id:
        ## edit the line, and change it to be done
            todo_parts = [todo_id,todo_text,"1"]
        put_back_together = ",".join(todo_parts)
        ## write to that file again
        todos_file.write(put_back_together + "\n")


view_incomplete_todos()
complete_todo('5')
view_incomplete_todos()


def add_todo(todo_text):
    ## read the file
    ## find the last ID number in the file
    ## append the new todo to the file
    pass


