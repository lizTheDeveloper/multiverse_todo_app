

def view_incomplete_todos():
    ## write a function that will read todos.csv
    todos_file = open("todos.csv", "r")
    file_contents = todos_file.read()
    # print(file_contents)
    todos = file_contents.split("\n")
    # print(todos)
    ## for every line in todos
    for todo in todos:
        # print(todo)
        todo_parts = todo.split(",")
        # print(todo_parts)
        if len(todo_parts) > 1:
            done = todo_parts[2]
            todo_text = todo_parts[1]
            todo_id = todo_parts[0]
            ## check to see if it's not done, if so:
            if done == "0":
                print(todo_id + ": " + todo_text)

view_incomplete_todos()


def complete_todo(completed_todo_id):
    ## read todos.csv
    todos_file = open("todos.csv", "r")
    file_contents = todos_file.read()
    todos = file_contents.split("\n")
    todos_file.close()

    ## open the file for writing
    todos_file = open("todos.csv", "w")
    ## find the todo
    for todo in todos:
        todo_parts = todo.split(",")
        # print(todo_parts)
        if len(todo_parts) > 1:
            done = todo_parts[2]
            todo_text = todo_parts[1]
            todo_id = todo_parts[0]
            if completed_todo_id == todo_id:
            ## edit the line, and change it to be done
                todo_parts = [todo_id,todo_text,"1"]
            put_back_together = ",".join(todo_parts)
            print(todo_parts)
            ## write to that file again
            todos_file.write(put_back_together + "\n")

complete_todo('5')



