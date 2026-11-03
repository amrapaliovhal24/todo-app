# To-Do List Web Application

A simple Flask to-do list app, built as part of an end-to-end cloud-native
deployment project using Docker, Amazon ECR, Amazon EKS, GitHub Actions
and Argo CD.

## Features
- Add new tasks
- Mark tasks as done / not done
- Delete tasks
- `/health` endpoint used for Kubernetes readiness checks

## Tech Stack
Python, Flask, Gunicorn, pytest

## Run Locally
```bash
git clone https://github.com/amrapaliovhal24/todo-app.git
cd todo-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://localhost:8080

## Run Tests
```bash
pytest
```

## Run with Docker
```bash
docker build -t todo-app .
docker run -p 8080:8080 todo-app
```

## Known Limitation
Tasks are stored in memory, so they reset when the app or pod restarts.

## Deployment
Pushing to `main` triggers GitHub Actions, which tests the app, builds a
Docker image, pushes it to Amazon ECR and updates the manifest in the
`todo-app-config` repository. Argo CD syncs that change to Amazon EKS. 