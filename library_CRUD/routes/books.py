# app/routes/book.py
from fastapi import APIRouter, Depends
from app.books import add_book, list_books, edit_book, remove_book
from app.database import get_db_connection
import sqlite3

router = APIRouter()
@router.post("/")
def create_book(title: str, author: str, genre: str, publication_year: int):
    return add_book( title, author, genre, publication_year)

@router.get("/")
def get_books(author: str = None, genre: str = None):
    return list_books(author, genre)

@router.put("/{book_id}")
def update_book(book_id: int, title: str = None, author: str = None, genre: str = None, publication_year: int = None):
    return edit_book( book_id, title, author, genre, publication_year)

@router.delete("/{book_id}")
def delete_book(book_id: int):
    return remove_book( book_id)
