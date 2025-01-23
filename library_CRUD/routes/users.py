# app/routes/users.py
from fastapi import APIRouter
from app.users import add_user, list_users, edit_user, remove_user

router = APIRouter()

@router.post("/")
def create_user(name: str, email: str, Phone: int):

    return add_user(name, email, Phone)

@router.get("/")
def get_users():

    return list_users()

@router.put("/{user_id}")
def update_user(user_id: int, name: str = None, email: str = None, Phone: int = None):

    return edit_user(user_id, name, email, Phone)

@router.delete("/{user_id}")
def delete_user(user_id: int):

    return remove_user(user_id)
