# 🏫 Student-Course Manager

**Student-Course Manager** is a modular, RESTful API built using **FastAPI** to manage students, courses, and enrollments within an educational institution. The API supports full CRUD operations, centralized error handling, and performance monitoring to simplify academic database workflows.

---

## 🚀 Features

- **👨‍🎓 Student Management**
  - Create, retrieve, update, and delete student records
  - List students by name or ID

- **📚 Course Management**
  - Add, retrieve, update, and delete course details
  - List courses by course name or ID

- **📝 Enrollment Management**
  - Create and remove enrollments linking students and courses
  - Retrieve all enrollment records

- **⚠️ Error Handling**
  - Centralized exception handling with structured error responses for better debugging

- **🧩 Middleware & Headers**
  - Custom middleware adds an `X-Process-Time` header to responses to track API performance

---

## 📁 Project Structure

```bash
college/
├── common/         # Shared utilities (e.g., DB setup)
├── students/       # Student models, schemas, repositories
├── courses/        # Course models, schemas, repositories
├── enrollments/    # Enrollment models, schemas, repositories
├── __init__.py
api.py              # API route definitions
main.py             # App entry point
demo3.db            # SQLite database
.env                # Environment variables
LICENSE             # License file
Images/             # Working of the project
```

## 📸 Example Screenshots

Below are some screenshots of the functionalities in action:

![1](Images/Screenshot%202025-06-22%20212813.png)  
Student Methods

![2](Images/Screenshot%202025-06-22%20212824.png)  
Course and Enrollment Methods

![Get course](Images/Screenshot%202025-06-22%20212938.png)  
Get course by course id

![Output of get course](Images/Screenshot%202025-06-22%20212949.png)  
Output of the query

---