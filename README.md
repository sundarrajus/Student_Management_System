# Student Management System using Python and Django

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap-purple?style=flat&logo=bootstrap)
![Chart.js](https://img.shields.io/badge/Charts-Chart.js-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## Overview

A fully functional **Student Management System** built using **Python and Django** — a web-based platform that allows administrators and staff to efficiently manage student records through a secure, role-based, and user-friendly interface.

This project demonstrates real-world full-stack development including user authentication, role-based access control, CRUD operations, interactive dashboards, and data visualization.

---

## Features

### Authentication & Access Control
- Secure **Login and Logout** system
- **Role-based access** — Admin sees all students, Staff manages only their own added students
- Session management and protected routes

### Dashboard
- Total students count
- Total staff count
- Student data insights and distribution charts using **Chart.js**

### Student Management (CRUD)
- **Add Student** — Name, Email, Age, Place, Gender, State, Skillset
- **View Student List** — Tabular format with search and pagination
- **Student Detail View** — Full profile on click
- **Edit Student** — Update existing records
- **Delete Student** — Secure record removal

### Additional Features
- Search students by name
- Pagination for large datasets
- Responsive UI using Bootstrap
- CSV export for data reporting

---

## Technologies Used

| Category | Technology |
|---|---|
| Language | Python 3.x |
| Backend Framework | Django |
| Frontend | HTML5, CSS3, Bootstrap |
| Database | SQLite |
| Data Visualization | Chart.js |
| Version Control | Git, GitHub |

---

## Project Structure

```
Student_Management_System_1/
│
├── student_management_system/
│   ├── app/
│   │   ├── models.py          # Student and User models
│   │   ├── views.py           # All view functions
│   │   ├── urls.py            # URL routing
│   │   └── migrations/        # Database migrations
│   │
│   ├── templates/
│   │   ├── login.html         # Login page
│   │   ├── register.html      # Registration page
│   │   ├── dashboard.html     # Admin dashboard
│   │   ├── add_student.html   # Add student form
│   │   ├── student_list.html  # Student listing with search
│   │   └── student_detail.html # Full student profile
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   └── requirements.txt
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/sundarrajus/Student_Management_System_1.git
cd Student_Management_System_1
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create superuser (Admin)**
```bash
python manage.py createsuperuser
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Open in browser**
```
http://127.0.0.1:8000/
```

---

## Sample Workflow

```
Admin logs in
      ↓
Dashboard — total students, staff, charts
      ↓
Add Student — fill name, email, age, skills
      ↓
Student List — search, paginate, view
      ↓
Edit / Delete — update or remove records
      ↓
Export CSV — download data for reporting
```

---

## Screenshots

> Add screenshots of your dashboard, student list, and add student form here

---

## Key Concepts Demonstrated

| Concept | Implementation |
|---|---|
| MVC Architecture | Django Models, Views, Templates |
| Authentication | Django built-in auth with session management |
| Role-based Access | Admin vs Staff permission control |
| CRUD Operations | Add, View, Edit, Delete student records |
| Data Visualization | Chart.js dashboard charts |
| Responsive Design | Bootstrap-based mobile-friendly UI |
| Search & Pagination | Filter students by name, paginated results |

---

## Future Enhancements

- Student profile photo upload
- Export student data to Excel
- Advanced dashboard analytics
- REST API integration using Django REST Framework
- Deploy to cloud platforms (Railway / Render / PythonAnywhere)
- Email notifications for new student additions

---

## Author

**Shavala Sundar Raju**
- GitHub: [@sundarrajus](https://github.com/sundarrajus)
- Email: shavalasundarraju@gmail.com
- LinkedIn: [Shavala Sundar Raju](https://linkedin.com/in/shavala-sundar-raju)

---

## License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

> "Built to solve a real problem — managing student data efficiently, securely, and at scale."
