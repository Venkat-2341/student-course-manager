# Student-Course Manager

Student-Course Manager is a RESTful API built with FastAPI for managing a college's students, courses, and enrollments. This API provides endpoints for CRUD operations across students, courses, and enrollment records, enabling efficient database management for educational institutions.

## Features
->Student Management: Create, retrieve, and list students by name or ID, helping manage the student database effortlessly.

->Course Management: Manage courses through endpoints to add, retrieve, and list courses by course name or ID.

->Enrollment Management: Handle enrollments, including creating new enrollments, deleting, and listing all enrollments.

->Error Handling: Detailed and structured error messages for easy debugging and handling of request failures.

->Middleware and Custom Headers: Includes middleware to track request processing times, adding an X-Process-Time header to responses.

->Custom Exception Handling: Centralized error handling to manage validation and runtime errors seamlessly.



## Project Structure
The project is organized into separate folders for different functional areas:

->college/common/: Common configurations and utilities, including database setup.

->college/students/: Handles all student-related models, schemas, and repository functions.

->college/courses/: Manages course-related models, schemas, and repository functions.

->college/enrollments/: Contains enrollment-related models, schemas, and repository functions.

## Technology Stack
1.FastAPI: The core framework for building and managing API routes.

2.SQLAlchemy: ORM for database interactions and query management.

3.Pydantic: Used for data validation and serialization.

4.Uvicorn: ASGI server for running the FastAPI application.