# 🚀 Django Project Setup Guide

This project is built using **Django (Python Web Framework)**.

Follow the steps below to run this project after downloading or cloning from GitHub.

---

## 📥 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project folder:

```bash
cd your-repository-name
```

---

## 🐍 2️⃣ Create Virtual Environment

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### ▶ Windows (PowerShell)
```bash
venv\Scripts\activate
```

### ▶ Windows (CMD)
```bash
venv\Scripts\activate.bat
```

### ▶ Mac/Linux
```bash
source venv/bin/activate
```

---

## 📦 3️⃣ Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install django
```

---

## 🗄 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 5️⃣ Create Superuser (Optional - For Admin Access)

```bash
python manage.py createsuperuser
```

Enter username, email, and password.

---

## ▶ 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

You will see:

```
Starting development server at http://127.0.0.1:8000/
```

Open in browser:

- Main Site → http://127.0.0.1:8000/
- Admin Panel → http://127.0.0.1:8000/admin/

---

## 🛑 7️⃣ Deactivate Virtual Environment

After finishing work:

```bash
deactivate
```

---

## 📁 Project Structure

```
project_root/
│── manage.py
│── requirements.txt
│── db.sqlite3
│
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app_name/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

---

## ⚙ Requirements

- Python 3.10+
- Django 4+
- pip

---

## 💡 Important Notes

- Always activate the virtual environment before running the project.
- Ensure `manage.py` is in the root directory.
- If facing dependency issues, delete `venv` and recreate it.
- Do not upload `venv/` folder to GitHub.

---


⭐ If you like this project, don't forget to give it a star!
