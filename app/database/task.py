from app.database import get_db


def fromat_output(results):
    out = []
    for result in results:
        res = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_done": result[3],
            "archived": result[4],
        }
        out.append(res)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE archived = 0", ())
    results = cursor.fetchall()
    cursor.close()
    return fromat_output(results)


def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,)) # the comma is important because it is a tuple in not a single value
    results = cursor.fetchall()
    if results:
        return fromat_output(results)[0]
    return None


def insert(task_data):
    statement = "INSERT INTO task (summary, description) VALUES (?, ?)"
    conn = get_db()
    conn.execute(statement, (
        task_data.get("summary"),
        task_data.get("description")
    ))
    conn.commit()


def update_by_id(task_data, task_id):
    statement = "UPDATE task SET summary = ?, description = ?, is_done = ?, archived = ? WHERE id = ?"
    conn = get_db()
    conn.execute(statement, (
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_data.get("archived"),
        task_id
    ))
    conn.commit()


def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
    conn.commit()
