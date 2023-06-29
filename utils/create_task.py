import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def create_task(sumary, description):
    task_data = {
        "summary": sumary,
        "description": description,
    }
    response = requests.post(BASE_URL, json=task_data)
    if response.status_code == 204:
        print("Task created successfully")
    else:
        print("Task creation failed")

if __name__ == "__main__":
    print("Create a task by filling out the prompts below:")
    summary = input("Summary: ")
    description = input("Description: ")
    create_task(summary, description)