import sqlite3
from fastapi import HTTPException
from datetime import datetime
from app.database import get_db_connection

def borrow_book(user_id: int, book_id: int, return_date: str):
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()

    # Check if the book exists and is available
    cursor.execute("SELECT id, available FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")  # Book does not exist

    if book["available"] == 0:
        raise HTTPException(status_code=400, detail="Book is currently not available")  # Book is borrowed

    # Check if the user exists
    cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")  # User does not exist

    # Validate return_date format
    try:
        expected_return_date = datetime.strptime(return_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid return_date format. Use YYYY-MM-DD")

    # Record the borrowing in the borrow_records table
    cursor.execute("""
        INSERT INTO borrow_records (book_id, user_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?)
    """, (book_id, user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), expected_return_date.strftime("%Y-%m-%d")))

    # Mark the book as borrowed in the books table
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))

    db.commit()
    db.close()

    return {"message": f"Book ID {book_id} successfully borrowed by User ID {user_id}. Return by {return_date}"}


def return_book(book_id: int):
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()

    # Check if the book is currently borrowed
    cursor.execute("""
        SELECT id FROM borrow_records
        WHERE book_id = ? AND is_returned = 0
    """, (book_id,))
    record = cursor.fetchone()

    if not record:
        raise HTTPException(status_code=404, detail="Borrow record not found or book already returned")

    # Update borrow record to mark the book as returned
    cursor.execute("""
        UPDATE borrow_records
        SET is_returned = 1, return_date = DATE('now')
        WHERE id = ?
    """, (record["id"],))

    # Mark the book as available in the books table
    cursor.execute("""
        UPDATE books
        SET available = 1
        WHERE id = ?
    """, (book_id,))

    db.commit()
    db.close()

    return {"message": "Book returned successfully"}
