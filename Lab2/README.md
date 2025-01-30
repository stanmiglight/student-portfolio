# User Management API

This is a FastAPI-based web service for managing a simple user database. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a list of users. Each user has a `user_id` and a `name`.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **CRUD Operations**: The API supports creating, reading, updating, and deleting users.
- **Pydantic Models**: Uses Pydantic for data validation and serialization.
- **Error Handling**: Provides appropriate error messages for invalid operations (e.g., user not found, duplicate user ID).

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/user-management-api.git
cd user-management-api
```

### Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```bash
pip install fastapi uvicorn pydantic
```

### Run the application:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading, so the server will restart whenever you make changes to the code.

## Usage

Once the server is running, you can access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Endpoints

### 1. `GET /users`
**Description**: Retrieve all users or a specific user by `user_id`.

**Query Parameter**:
- `user_id` (optional): The ID of the user to retrieve.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/users"
```

or

```bash
curl -X GET "http://127.0.0.1:8000/users?user_id=1"
```

**Example Response:**

```json
{
  "status": "ok",
  "result": [
    {"user_id": 1, "name": "John Doe"},
    {"user_id": 2, "name": "Jane Smith"},
    {"user_id": 3, "name": "Alice Johnson"}
  ]
}
```

or

```json
{
  "status": "ok",
  "result": {"user_id": 1, "name": "John Doe"}
}
```

### 2. `POST /users`
**Description**: Create a new user.

**Request Body:**

```json
{
  "user_id": 4,
  "name": "New User"
}
```

**Example Request:**

```bash
curl -X POST "http://127.0.0.1:8000/users" -H "Content-Type: application/json" -d '{"user_id": 4, "name": "New User"}'
```

**Example Response:**

```json
{
  "status": "ok",
  "result": {"user_id": 4, "name": "New User"}
}
```

### 3. `PUT /users/{user_id}`
**Description**: Update an existing user by `user_id`.

**Path Parameter:**
- `user_id`: The ID of the user to update.

**Request Body:**

```json
{
  "user_id": 1,
  "name": "Updated Name"
}
```

**Example Request:**

```bash
curl -X PUT "http://127.0.0.1:8000/users/1" -H "Content-Type: application/json" -d '{"user_id": 1, "name": "Updated Name"}'
```

**Example Response:**

```json
{
  "status": "ok",
  "updated_data": {"user_id": 1, "name": "Updated Name"}
}
```

### 4. `DELETE /users/{user_id}`
**Description**: Delete a user by `user_id`.

**Path Parameter:**
- `user_id`: The ID of the user to delete.

**Example Request:**

```bash
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

**Example Response:**

```json
{
  "status": "ok",
  "removed_data": {"user_id": 1, "name": "John Doe"}
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- **Sir Paulo** for the idea!
- **FastAPI** for providing an easy-to-use and high-performance web framework.
- **Pydantic** for data validation and serialization.
- **Python** for being awesome.
