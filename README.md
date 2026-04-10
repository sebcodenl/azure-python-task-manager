# Azure Python Task Manager

A Python web application built with Flask, hosted on Azure App Service, and automatically deployed via GitHub Actions.

🔗 **Live demo:** [Open app](https://sebas-task-manager-app-ddf0gvfqhnhzcbaf.westeurope-01.azurewebsites.net/)

---

## 📌 About this project

This is my second Azure project. I built a task manager application with a Python (Flask) backend and an HTML/CSS frontend. The app runs fully on Microsoft Azure and is automatically deployed on every push to the main branch.

---

## 🛠️ Technologies used

- Python (Flask)
- HTML & CSS
- Azure App Service (Linux, Python 3.12)
- GitHub Actions (CI/CD)
- Git & GitHub

---

## ⚙️ Features

- Add tasks via a web form
- Dynamically display tasks
- Clean and simple UI

---

## ☁️ Azure setup

| Component | Details |
|---|---|
| Service | Azure App Service |
| OS | Linux |
| Runtime | Python 3.12 |
| Startup command | `gunicorn app:app` |
| Deployment | GitHub Actions |

---

## 🔄 CI/CD Pipeline

Every push to the `main` branch automatically:
1. Builds the application
2. Installs dependencies
3. Deploys to Azure App Service

---

## 💡 What I learned

- How to build a Python web app with Flask
- How to deploy to Azure App Service
- How to set up a CI/CD pipeline with GitHub Actions
- How to troubleshoot deployment issues (credentials, startup commands)

---

## 🚧 Future improvements

- [ ] Store tasks in a database (Azure Table Storage or Azure SQL)
- [ ] Add delete and edit functionality
- [ ] Add user authentication
- [ ] Improve UI/UX

---

## 👨‍💻 About me

I am working towards becoming an Azure specialist and actively building my portfolio.
This project is part of that journey 🚀