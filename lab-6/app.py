from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route("/")
def home():
    return "Welcome to Todo API"

@app.route("/todos", methods=["POST"])
def add_todo():

    data = request.get_json()

    new_task = {
        "id": len(todos) + 1,
        "title": data["title"],
        "completed": False
    }

    todos.append(new_task)

    return jsonify(new_task)


@app.route("/todos", methods=["GET"])
def get_all_todos():
    return jsonify(todos)


@app.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):

    for todo in todos:

        if todo["id"] == id:
            return jsonify(todo)

    return jsonify({"error":"Task not found"}),404


@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):

    data=request.get_json()

    for todo in todos:

        if todo["id"]==id:

            todo["title"]=data["title"]
            todo["completed"]=data["completed"]

            return jsonify(todo)

    return jsonify({"error":"Task not found"}),404


@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):

    for todo in todos:

        if todo["id"]==id:

            todos.remove(todo)

            return jsonify({"message":"Task deleted successfully"})

    return jsonify({"error":"Task not found"}),404


if __name__=="__main__":
    app.run(debug=True)