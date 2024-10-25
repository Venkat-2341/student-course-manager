import time 
import asyncio

from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from college.common import Base, engine, get_db
from college.students import Student, StudentCreate, StudentRepository
from college.courses import Course, CourseCreate, CoursesRepository
from college.enrollments import Enrollment, EnrollmentCreate, EnrollmentRepository

app = FastAPI(
    title="Student-Course-Manager",
    description="Fast API rest service to manage various students, courses and enrollments in a college",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validate_exception_handle(request, error):
    base_error_message = f"Failed to Handle the Request and Execute: {
        request.method}: {request.url}"

    return JSONResponse(
        status_code=400,
        content={
            "message": f"{base_error_message}, Detail :{error}"
        }
    )


@app.middleware("http")
async def add_process_time_header(request, call_next):
    print("Inside the Middleware ...")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(f"{process_time:0.4f} Second(s)")

    return response


@app.post("/students",
          tags=["Student"],
          response_model=Student,
          status_code=201)
async def create_student(new_student: StudentCreate, db:Session=Depends(get_db)):
        """
        Create a Student and store it in the Database.
        """
        db_item = StudentRepository.fetch_with_name(db,new_student.first_name, new_student.last_name)
    
        if db_item is not None:
            # Student alredy exists in the database.
            raise HTTPException(
                status_code=400,
                detail="Student already exists"
            )
        
        await StudentRepository.create(db, new_student)


@app.get("/students/{first_name}/{last_name}",
         tags=["Student"],
         response_model=Student,
         status_code=201)
def get_student_by_name(first_name: str, last_name:str, db:Session = Depends(get_db)):
    
    db_item = StudentRepository.fetch_with_name(db, first_name, last_name)
    
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not found!!"
        )
    return db_item


@app.get("/students/{student_id}",
         tags=["Student"],
         response_model=Student,
         status_code=201)
def get_student_by_id(id:int, db:Session = Depends(get_db)):
    
    db_item = StudentRepository.fetch_with_id(db, id)
    
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not found!!"
        )
    
    return db_item


@app.get("/students",
         tags=["Student"],
         response_model=List[Student],
         status_code=201)
def get_all_students(db:Session = Depends(get_db)):
    
    db_item = StudentRepository.fetch_all(db)
    
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Database not found"
        )
    
    return db_item


@app.post("/courses",
          tags=["Course"],
          response_model=Course,
          status_code=201)
async def create_course(new_course: CourseCreate, db:Session=Depends(get_db)):
    
    db_item = CoursesRepository.fetch_with_name(db, new_course.course_name)
    
    if db_item is not None:
        # Course alredy exists in the database.
        raise HTTPException(
            status_code=400,
            detail="Course already exists"
        )
        
    await CoursesRepository.create(db, new_course)


@app.get("/courses/{course_id}",
         tags=["Course"],
         response_model=Course,
         status_code=201)
def get_course_by_id(id:int, db:Session = Depends(get_db)):
    
    db_item = CoursesRepository.fetch_with_id(db, id)
    
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Course Not found!!"
        )
    
    return db_item


@app.get("/courses/{course_name}",
         tags=["Course"],
         response_model=Course,
         status_code=201)
def get_course_by_name(name:str, db:Session = Depends(get_db)):
    
    db_item = CoursesRepository.fetch_with_name(db, name)
    
    if db_item is None:
        raise HTTPException(
            status_code=404,
            detail="Course Not found!!"
        )
    
    return db_item


@app.post("/enrollments",
          tags=["Enrollment"],
          response_model=Enrollment,
          status_code=201)
async def create_enrollment(new_enrollment: EnrollmentCreate, db:Session=Depends(get_db)):
    
    db_item = EnrollmentRepository.fetch_with_name(db, new_enrollment.student_id, new_enrollment.course_id)
    # check if the (student_id, course_id) pair is already present
    # if it is present then there that student has already enrolled in that particular course.
    
    if db_item is not None:
        # Course alredy exists in the database.
        raise HTTPException(
            status_code=400,
            detail="Course already exists"
        )
        
    await EnrollmentRepository.create(db, new_enrollment)
    

@app.delete("/enrollments",
            tags=["Enrollment"],
            response_model=Enrollment,
            status_code=201)
def delete_enrollment(student_id:int, course_id:int, db:Session= Depends(get_db)):
    
    db_item = EnrollmentRepository.delete(db, student_id, course_id)
    
    if db_item is None:
        raise HTTPException(
            status_code=400,
            detail="Student has not been enrolled in the particular course"
        )
    
    return {"message": "Enrollment successfully deleted"}



