
# Library Management System API

  

## Project Overview

  

The Library Management System is a robust, RESTful API built using FastAPI and SQLite, designed to streamline library operations by providing comprehensive book, user, and borrowing management capabilities.

  

## Key Features

  

### Book Management

-  **Create**: Add new books to the library catalog

-  **Retrieve**: List and search books by various criteria

-  **Update**: Modify existing book information

-  **Delete**: Remove books from the system

  

### User Management

-  **Create**: Register new library users

-  **Retrieve**: View user information

-  **Update**: Modify user details

-  **Delete**: Remove user accounts

  

### Borrowing Workflow

-  **Borrow Books**: Allow users to check out books

-  **Return Books**: Track and manage book returns

-  **Availability Tracking**: Monitor book availability in real-time

  

## Technical Architecture

  

### Database Structure

The system utilizes an SQLite database with the following schema:

  



| `books` | Store book catalog information |

| `users` | Maintain user account details |

| `borrow_records`| Track book borrowing and return status |

  

## System Requirements

  

### Prerequisites

- Python 3.8+

- FastAPI

- SQLite

- python-dotenv

  

### Installation Steps

  

1.  **Repository Cloning**

```bash

git clone https://github.com/your-username/library-management-system.git

cd library_CRUD
```

  

2.  **Dependency Installation**

```bash

pip install -r requirements.txt

```

  

3.  **Environment Configuration**

Create a `.env` file in the root directory:

```

DATABASE_URL=path_to_your_database.db

```

  

4.  **Launch Application**

```bash

uvicorn app.main:app --reload

```

  

## API Endpoints

  

### Books Endpoints

  

| Method | Endpoint | Description | Request Body Parameters |



| POST | `/books/` | Create a new book | `title`, `author`, `genre`, `publication_year` |

| GET | `/books/` | Retrieve books | Optional: `author`, `genre` |

| PUT | `/books/{id}` | Update a book | `title`, `author`, `genre`, `publication_year` |

| DELETE | `/books/{id}` | Delete a book | None |

  

### Users Endpoints

  

| Method | Endpoint | Description | Request Body Parameters |



| POST | `/users/` | Create a new user | `name`, `email`, `phone` |

| GET | `/users/` | Retrieve users | None |

| PUT | `/users/{id}` | Update a user | `name`, `email`, `phone` |

| DELETE | `/users/{id}` | Delete a user | None |

  

### Borrowing Endpoints

  

| Method | Endpoint | Description | Request Body Parameters |


| POST | `/borrow/` | Borrow a book | `user_id`, `book_id`, `return_date` |

| PUT | `/borrow/return/{id}` | Return a borrowed book | `user_id`, `book_id` |

  

## Error Handling

  

The API provides comprehensive error responses:

  

-  **500 Internal Server Error**: Database connection failures

-  **404 Not Found**: Resource (book, user, borrow record) not exists

-  **400 Bad Request**: Invalid input data

  

## Example Request Payloads

  

### Create Book

```json

{

"title": "The Great Gatsby",

"author": "F. Scott Fitzgerald",

"genre": "Fiction",

"publication_year": 1925

}

```

  

### Update User

```json

{

"name": "Jane Smith",

"email": "jane.smith@example.com",

"phone": "+9876543210"

}

```

  

### Borrow Book

```json

{

"user_id": 1,

"book_id": 101,

"return_date": "2025-02-20"

}

```

  



