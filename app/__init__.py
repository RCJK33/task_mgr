from flask import Flask, request
from app.database import task

app = Flask(__name__)

@app.get("/tasks")
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True,
    }
    return out

@app.get("/tasks/<int:pk>")
def get_task_by_id(pk):
    taskFin = task.select_by_id(pk)
    out = {
        "task": taskFin,
        "ok": True,
    }
    if taskFin == None:
        out["ok"] = False
        out["message"] = "Task not found"
    return out

@app.post("/tasks")
def create_task():
    raw_data = request.get_json()
    task.insert(raw_data)
    return "", 204

@app.put("/tasks/<int:pk>")
def update_task(pk):
    raw_data = request.get_json()
    task.update_by_id(raw_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204