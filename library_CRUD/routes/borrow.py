from fastapi import APIRouter
from app.borrow import borrow_book, return_book

router = APIRouter()

@router.post("/")
def borrow(user_id: int, book_id: int, return_date: str):
    """
    Allow a user to borrow a book if it's available and specify a return date.
    """
    return borrow_book(user_id, book_id, return_date)


@router.put("/return/{borrow_id}")
def return_borrowed_book(borrow_id: int):
    """
    Mark a book as returned by its borrow record ID.
    """
    return return_book(borrow_id)
