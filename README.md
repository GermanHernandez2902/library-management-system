# 📚 Library Management System

A web-based system to manage digital libraries, book loans, and student/admin access built using **Django**. Simple, clean and fully functional — designed for educational purposes and real-world practice.

![Screenshot](https://img.shields.io/badge/Django-4.2-success?style=for-the-badge&logo=django)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blue?style=for-the-badge&logo=render)

## 🚀 Live Demo

👉 [Try the Live App Here](https://library-management-system-zce5.onrender.com)

> ⚠️ The Render free plan may take a few seconds to wake up the service.

---

## ✨ Features

- 👤 **Admin Portal**  
  - Add/view books  
  - Issue books to students  
  - View issued books and student profiles  

- 🎓 **Student Portal**  
  - View issued books  
  - See issue/return dates and fines  
  - Register & Login

- 🔐 Auth system using Django's built-in users/groups

---

## 🛠️ Tech Stack

- **Backend**: Django 4.2, PostgreSQL, Gunicorn  
- **Frontend**: HTML5, Bootstrap 4, Crispy Forms  
- **Deployment**: Render, GitHub

---

## ⚙️ Setup Locally

```bash
git clone https://github.com/GermanHernandez2902/library-management-system.git
cd library-management-system
python -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Then go to http://127.0.0.1:8000/

📁 Folder Structure
csharp
Copiar
Editar
library-management-system/
│
├── library/               # Django app
├── librarymanagement/     # Django project
├── templates/             # HTML templates
├── static/                # Static files
├── requirements.txt
└── manage.py


📜 License
This project is open-source and free to use under the MIT License.

yaml
Copiar
Editar

---

### ✅ ¿Qué hacer ahora?

1. Guarda este contenido como `README.md` en la raíz del proyecto.
2. Luego en tu terminal:

```bash
git add README.md
git commit -m "Docs: add professional README with demo link"
git push origin main
