from app import app, tasks, counter


def setup_function():
    tasks.clear()
    counter["next_id"] = 1


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200


def test_add_task():
    c = app.test_client()
    c.post("/add", data={"task": "Learn EKS"})
    assert len(tasks) == 1 and tasks[0]["text"] == "Learn EKS"


def test_toggle_and_delete():
    c = app.test_client()
    c.post("/add", data={"task": "Test"})
    c.post("/toggle/1")
    assert tasks[0]["done"] is True
    c.post("/delete/1")
    assert tasks == []