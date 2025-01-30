# Multi-API FastAPI Repository

This repository contains four distinct FastAPI projects, each demonstrating different functionalities and use cases. Below is a brief overview of each project and instructions on how to set up and run them.

## Projects Overview

### 1. Factorial Calculator API
**Description:** A simple API that calculates the factorial of a given integer.

**Endpoints:**
- `GET /factorial/{starting_number}`: Returns the factorial of the provided integer.

**File:** `main.py`

---

### 2. User Management API
**Description:** A CRUD API for managing a list of users. Supports creating, reading, updating, and deleting users.

**Endpoints:**
- `GET /users`: Retrieve all users or a specific user by `user_id`.
- `POST /users`: Create a new user.
- `PUT /users/{user_id}`: Update an existing user.
- `DELETE /users/{user_id}`: Delete a user.

**File:** `main.py`

---

### 3. External API Integration
**Description:** Demonstrates how to interact with an external API ([JSONPlaceholder](https://jsonplaceholder.typicode.com/)) to fetch and manipulate data.

**Endpoints:**
- `GET /posts/`: Retrieve all posts or a specific post by `postId`.
- `GET /comments/`: Retrieve all comments or comments for a specific post by `postId`.
- `GET /formatted_posts/{userID}`: Retrieve and format posts for a specific user.
- `GET /formatted_comment/{postID}`: Retrieve and format comments for a specific post.
- `GET /detailed_post/{userID}`: Retrieve detailed posts and comments for a specific user.

**File:** `main.py`

---

### 4. Task Management API (v1 and v2)
**Description:** A task management system with two versions (v1 and v2) of the API. Each version has its own database and supports CRUD operations on tasks.

**Endpoints:**
- `GET /apiv1/`, `GET /apiv2/`: Welcome messages for API v1 and v2.
- `GET /apiv1/tasks/`, `GET /apiv2/tasks/`: Retrieve all tasks in v1 or v2.
- `GET /apiv1/tasks/{task_id}`, `GET /apiv2/tasks/{task_id}`: Retrieve a specific task by `task_id`.
- `POST /apiv1/tasks/`, `POST /apiv2/tasks/`: Create a new task.
- `DELETE /apiv1/tasks/{task_id}`, `DELETE /apiv2/tasks/{task_id}`: Delete a task by `task_id`.
- `PATCH /apiv1/tasks/{task_id}`, `PATCH /apiv2/tasks/{task_id}`: Update a task by `task_id`.

**File:** `main.py`

---

## Installation

### Clone the repository:
```bash
git clone https://github.com/stanmiglight/student-portfolio.git
cd multi-api-fastapi-repo
```

### Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Create a `.env` file (for Task Management API):
Create a `.env` file in the root directory and add your API key:
```env
API_KEY=your_api_key_here
```

---

## Usage
Once the server is running, you can access the APIs at `http://127.0.0.1:8000`. Use tools like `curl`, Postman, or your browser to interact with the endpoints.

### API Key Authentication (Task Management API)
For the Task Management API, include the API key in the `Authorization` header of your requests:
```bash
Authorization: Bearer your_api_key_here
```

---

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


---

## Acknowledgments
- Sir Paulo for everything!
- [FastAPI](https://fastapi.tiangolo.com/) for providing an easy-to-use and high-performance web framework.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) for providing a free fake API for testing and prototyping.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
- **Python** for being awesome.
