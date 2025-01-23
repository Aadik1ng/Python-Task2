from fastapi import HTTPException
from app.database import get_db_connection,check_and_create_db
import sqlite3

def add_book(title: str, author: str, genre: str, publication_year: int):
    db = get_db_connection()  
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, genre, publication_year)
        VALUES (?, ?, ?, ?)
    """, (title, author, genre, publication_year))
    db.commit()
    db.close()  
    return {"message": "Book added successfully"}

def list_books(author: str = None, genre: str = None):
    db = get_db_connection()  
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    query = "SELECT * FROM books WHERE 1=1"
    params = []

    if author:
        query += " AND author = ?"
        params.append(author)

    if genre:
        query += " AND genre = ?"
        params.append(genre)

    cursor.execute(query, tuple(params))
    books = cursor.fetchall()
    db.close()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return [{"id": book["id"], "title": book["title"], "author": book["author"], "genre": book["genre"], "publication_year": book["publication_year"]} for book in books]

def edit_book(book_id: int, title: str = None, author: str = None, genre: str = None, publication_year: int = None):
    db = get_db_connection()  
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    updates = []
    params = []

    if title:
        updates.append("title = ?")
        params.append(title)
    if author:
        updates.append("author = ?")
        params.append(author)
    if genre:
        updates.append("genre = ?")
        params.append(genre)
    if publication_year:
        updates.append("publication_year = ?")
        params.append(publication_year)

    if not updates:
        raise HTTPException(status_code=400, detail="No data to update")

    query = f"UPDATE books SET {', '.join(updates)} WHERE id = ?"
    params.append(book_id)
    cursor.execute(query, tuple(params))
    db.commit()
    db.close()

    return {"message": "Book updated successfully"}

def remove_book(book_id: int):
    db = get_db_connection()  
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    if book_id:
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    else:
        cursor.execute("SELECT COUNT(*) FROM books")
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("No books found in the database.")
        else:
            cursor.execute("DELETE FROM books")
            
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='books'")
            
    db.commit()
    db.close()
    
    return {"message": "Book(s) deleted successfully (if any existed), and ID counter reset if necessary."}
