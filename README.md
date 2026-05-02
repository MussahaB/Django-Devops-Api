# Django-Devops-Api
# Django DevOps API

A Django REST API Website built with a complete DevOps workflow including containerization, CI/CD automation, and cloud deployment.

---

## 🚀 Live Demo

🔗 https://django-devops-api.onrender.com

---

## 🛠 Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions
* **Deployment:** Render

---

## ⚙️ Features

* Task management REST API (CRUD operations)
* Django admin panel for managing data
* Fully containerized using Docker
* PostgreSQL database integration
* CI pipeline with linting and testing

---

## 📁 Project Structure

```
django-devops-api/
│
├── config/             # Django settings & main config
├── tasks/              # Task app (models, views, serializers)
├── users/              # User-related logic
├── projects/           # Project module
├── .github/workflows/  # CI/CD pipeline
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── .flake8
└── README.md
```

---

## 🧪 CI/CD Pipeline

This project uses GitHub Actions for continuous integration.

On every push to `main` branch:

* Code is checked out
* Python environment is set up
* Dependencies are installed
* Code linting is performed using flake8
* Database migrations are tested
* Unit tests are executed

---

## 🐳 Running Locally with Docker

Clone the repository:

```
git clone <your-repo-url>
cd django-devops-api
```

Build and run containers:

```
docker compose up --build
```

Run migrations (if needed):

```
docker compose exec web python manage.py migrate
```

Access the app:

```
http://localhost:8000
```

---

## 🔐 Environment Variables

Create a `.env` file or configure environment variables:

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
ALLOWED_HOSTS=
```

---

## 📌 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | /api/tasks/      | List all tasks    |
| POST   | /api/tasks/      | Create a new task |
| PUT    | /api/tasks/<id>/ | Update a task     |
| DELETE | /api/tasks/<id>/ | Delete a task     |

---

## 🔧 Deployment

The application is deployed on Render using Docker.

Deployment includes:

* Docker-based build process
* Managed PostgreSQL database
* Environment variable configuration
* Automatic deployment on code push

---

## 📚 Key Learnings

* Containerizing Django applications with Docker
* Managing multi-service architecture with PostgreSQL
* Implementing CI/CD pipelines using GitHub Actions
* Debugging real-world deployment issues
* Deploying production-ready applications on cloud platforms

---

## 👨‍💻 Author

Built by Mussahab — Backend Developer specializing in Python and web applications.

---
