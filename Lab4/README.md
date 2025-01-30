## Task Management API (v1 and v2)

This project is a FastAPI-based task management system that provides two versions of the API (v1 and v2). Each version has its own database and endpoints for performing CRUD (Create, Read, Update, Delete) operations on tasks. The API is secured using an API key stored in an `.env` file.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **API Key Authentication**: Secures endpoints using an API key stored in an `.env` file.
- **CRUD Operations**: Supports creating, reading, updating, and deleting tasks.
- **Versioning**: Provides two versions of the API (v1 and v2) with separate databases.
- **Error Handling**: Includes proper error handling for invalid requests, missing tasks, and unauthorized access.

## Installation

### Clone the repository:

```bash
git clone https://github.com/stanmiglight/student-portfolio.git
cd lab4
```

### Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```bash
pip install fastapi uvicorn python-dotenv
```

### Create a `.env` file:

Create a `.env` file in the root directory and add your API key:

```env
API_KEY=your_api_key_here
```

### Run the application:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading, so the server will restart whenever you make changes to the code.

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000`.

### API Key Authentication

All endpoints require an API key for authentication. Include the API key in the `Authorization` header of your requests:

```
Authorization: Bearer your_api_key_here
```

## Endpoints

### API v1

#### `GET /apiv1/`

**Description**: Welcome message for API v1.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/apiv1/" -H "Authorization: Bearer your_api_key_here"
```

**Example Response:**

```json
{
  "message": "Welcome to API v1"
}
```

#### `GET /apiv1/tasks/`

**Description**: Retrieve all tasks in v1.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/apiv1/tasks/" -H "Authorization: Bearer your_api_key_here"
```

**Example Response:**

```json
{
  "status": "ok",
  "tasks": [
    {
      "task_id": 1,
      "task_title": "Test 1",
      "task_desc": "Complete FastAPI basics",
      "is_finished": false
    }
  ]
}
```

#### `GET /apiv1/tasks/{task_id}`

**Description**: Retrieve a specific task by `task_id` in v1.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/apiv1/tasks/1" -H "Authorization: Bearer your_api_key_here"
```

**Example Response:**

```json
{
  "status": "ok",
  "task": {
    "task_id": 1,
    "task_title": "Test 1",
    "task_desc": "Complete FastAPI basics",
    "is_finished": false
  }
}
```

#### `POST /apiv1/tasks/`

**Description**: Create a new task in v1.

**Request Body:**

```json
{
  "task_title": "New Task",
  "task_desc": "This is a new task"
}
```

**Example Request:**

```bash
curl -X POST "http://127.0.0.1:8000/apiv1/tasks/" -H "Authorization: Bearer your_api_key_here" -H "Content-Type: application/json" -d '{"task_title": "New Task", "task_desc": "This is a new task"}'
```

**Example Response:**

```json
{
  "status": "ok",
  "task": {
    "task_id": 2,
    "task_title": "New Task",
    "task_desc": "This is a new task",
    "is_finished": false
  }
}
```

#### `DELETE /apiv1/tasks/{task_id}`

**Description**: Delete a task by `task_id` in v1.

**Example Request:**

```bash
curl -X DELETE "http://127.0.0.1:8000/apiv1/tasks/1" -H "Authorization: Bearer your_api_key_here"
```

**Example Response:**

```json
{
  "status": "ok",
  "message": "Task deleted successfully"
}
```

#### `PATCH /apiv1/tasks/{task_id}`

**Description**: Update a task by `task_id` in v1.

**Request Body (optional fields):**

```json
{
  "task_title": "Updated Task",
  "task_desc": "This is an updated task",
  "is_finished": true
}
```

**Example Request:**

```bash
curl -X PATCH "http://127.0.0.1:8000/apiv1/tasks/1" -H "Authorization: Bearer your_api_key_here" -H "Content-Type: application/json" -d '{"task_title": "Updated Task", "is_finished": true}'
```

**Example Response:**

```json
{
  "status": "ok",
  "task": {
    "task_id": 1,
    "task_title": "Updated Task",
    "task_desc": "Complete FastAPI basics",
    "is_finished": true
  }
}
```

### API v2

The endpoints for API v2 (`/apiv2/`) are identical to those of API v1, but they operate on a separate database (`task_db_v2`). Refer to the v1 documentation for usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- **Sir Paulo** for the idea!
- **FastAPI** for providing an easy-to-use and high-performance web framework.
- **python-dotenv** for managing environment variables.
- **Python** for being awesome.
