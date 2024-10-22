import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///demo2.db", 
                       connect_args={
                           "check_same_thread":False
                       },
                       echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, 
                       autoflush=False,
                       autocommit=False)

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()