import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def update_task(id, summary, description,is_done=0,archived=0):
    task_data = {
        "summary": summary,
        "description": description,
        "is_done": is_done,
        "archived": archived,
    }
    response = requests.put(f"{BASE_URL}/{id}", json=task_data)
    if response.status_code == 204:
        print("Task updated successfully")
    else:
        print("Task update failed")

if __name__ == "__main__":
    print("Update a task by filling out the prompts below:")
    id = input("Id: ")
    summary = input("Summary: ")
    description = input("Description: ")
    is_done = input("Done (True=1/False=0): ")
    archived = input("Archived (True=1/False=0): ")
    update_task(id,summary, description,is_done,archived)
