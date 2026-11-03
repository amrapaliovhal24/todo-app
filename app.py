import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []
counter = {"next_id": 1}
APP_TITLE = os.getenv("APP_TITLE", "My To-Do List")


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, title=APP_TITLE)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("task", "").strip()
    if text:
        tasks.append({"id": counter["next_id"], "text": text, "done": False})
        counter["next_id"] += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)