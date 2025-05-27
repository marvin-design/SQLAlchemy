# Object Relations Code Challenge - Articles

## Project Overview

This project models the relationships between **Authors**, **Articles**, and **Magazines**, with data persisted in a SQL database. It demonstrates core object-oriented programming concepts and raw SQL integration within Python classes.

- An **Author** can write many **Articles**.
- A **Magazine** can publish many **Articles**.
- An **Article** belongs to both an **Author** and a **Magazine**.
- The **Author**-**Magazine** relationship is many-to-many.

This project includes implementation of:
- SQL schema for Authors, Articles, and Magazines.
- Python model classes with methods for CRUD operations and relationship queries.
- Transaction handling and error management.
- Unit tests validating functionality.

---

## Features

- Create, read, update, and delete Authors, Articles, and Magazines.
- Query articles by author or magazine.
- Retrieve all magazines an author has contributed to.
- Find contributors and article titles for a magazine.
- Complex SQL queries like magazines with multiple authors and top publishers.
- Transactional support for multi-step operations.
- Input validation and SQL injection protection.

---

## Technology Stack

- **Python 3.x**
- **SQLite** (default) or **PostgreSQL** (optional)
- **Raw SQL** queries for database interaction
- **pytest** for unit testing
- Virtual environment with `pipenv` or `venv`

---

## Setup Instructions

### 1. Environment Setup

**Option 1: Pipenv**
```bash
pipenv install pytest sqlite3
pipenv shell
