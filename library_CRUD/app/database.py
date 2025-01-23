import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv('DATABASE_URL')  

def check_and_create_db():
    if not os.path.exists(DATABASE_PATH):
        print(f"Database {DATABASE_PATH} not found. Creating a new one.")
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            conn.close()  
            print(f"Database {DATABASE_PATH} created successfully.")
        except Exception as e:
            print(f"Error creating database: {e}")
    else:
        print(f"Database {DATABASE_PATH} already exists.")

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row  
        return conn
    except sqlite3.OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None  

def create_tables():
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    publication_year INTEGER NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    Phone INTEGER NOT NULL
                )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrow_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrow_date TEXT NOT NULL,
                return_date TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (book_id) REFERENCES books (id)
            )
        """)

        

            print("Tables created successfully or already exist.")
    except sqlite3.OperationalError as e:
        print(f"Database error while creating tables: {e}")
