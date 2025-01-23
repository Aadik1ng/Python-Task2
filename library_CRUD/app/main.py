# app/main.py
from fastapi import FastAPI
from app.database import create_tables,check_and_create_db
from routes.books import router as book_router
from routes.users import router as user_router
from routes.borrow import router as borrow_router


app = FastAPI()
check_and_create_db()
create_tables()

app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(borrow_router, prefix="/borrow", tags=["Borrow"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API"}
