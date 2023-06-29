import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    if response.status_code == 204:
        print("Task deleted successfully")
    else:
        print("Task deletion failed")

if __name__ == "__main__":
    print("Delete a task by filling out the prompts below:")
    id = input("Id: ")
    delete_task(id)