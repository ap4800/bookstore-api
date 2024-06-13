# Bookstore RESTful API

This is a RESTful API for a bookstore built using Flask. It includes features for CRUD operations on books and user authentication with JWT. The API is documented with Swagger.

## Features

- User registration and login
- JWT authentication
- CRUD operations for books
- API documentation with Swagger

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/bookstore-api.git
    cd bookstore-api
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the application:
    ```sh
    python run.py
    ```

## Usage

### Register a new user
```sh
curl -X POST http://localhost:5000/auth/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
