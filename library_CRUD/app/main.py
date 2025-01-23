# app/main.py
from fastapi import FastAPI
from app.database import create_tables,check_and_create_db
from routes.books import router as book_router

# Initialize FastAPI
app = FastAPI()
check_and_create_db()
# Create tables when the app starts
create_tables()

# Include the book routes
app.include_router(book_router, prefix="/books", tags=["Books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API"}
