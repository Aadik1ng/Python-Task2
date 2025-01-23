from fastapi import HTTPException
from app.database import get_db_connection

def add_user(name: str, email: str, Phone: int):
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO users (name, email, Phone)
        VALUES (?, ?, ?)
    """, (name, email, Phone))
    db.commit()
    db.close()
    return {"messPhone": "User added successfully"}

def list_users():
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return [{"id": user["id"], "name": user["name"], "email": user["email"], "Phone": user["Phone"]} for user in users]

def edit_user(user_id: int, name: str = None, email: str = None, Phone: int = None):
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    updates = []
    params = []

    if name:
        updates.append("name = ?")
        params.append(name)
    if email:
        updates.append("email = ?")
        params.append(email)
    if Phone:
        updates.append("Phone = ?")
        params.append(Phone)

    if not updates:
        raise HTTPException(status_code=400, detail="No data to update")

    query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
    params.append(user_id)
    cursor.execute(query, tuple(params))
    db.commit()
    db.close()

    return {"messPhone": "User updated successfully"}

def remove_user(user_id: int):
    db = get_db_connection()
    if db is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    db.close()

    return {"messPhone": "User deleted successfully"}
