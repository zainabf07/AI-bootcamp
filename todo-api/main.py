from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
class UpdateTodo(BaseModel):
    title: str
    completed: bool
@app.get("/")
def home():
    return {"message": "Welcome to Todo API"}
@app.post("/todos")
def add_todo(todo: Todo):

    new_task = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False
    }

    todos.append(new_task)

    return new_task


@app.get("/todos")
def get_all_todos():
    return todos

@app.get("/todos/{id}")
def get_todo(id: int):

    for todo in todos:

        if todo["id"] == id:
            return todo

    return {"error": "Task not found"}

@app.put("/todos/{id}")
def update_todo(id: int, updated_todo: UpdateTodo):

    for todo in todos:

        if todo["id"] == id:
            todo["title"] = updated_todo.title
            todo["completed"] = updated_todo.completed
            return todo

    return {"error": "Task not found"}
@app.delete("/todos/{id}")
def delete_todo(id: int):

    for todo in todos:

        if todo["id"] == id:
            todos.remove(todo)
            return {"message": "Task deleted successfully"}

    return {"error": "Task not found"}