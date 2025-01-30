# External API Integration with FastAPI

This project demonstrates how to interact with an external API using FastAPI. The goal is to fetch data from an external API, manipulate it using Python, and return the results in a structured JSON format. The project also includes an example of creating a new API endpoint that combines data from multiple external API calls.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **External API Integration**: Fetches data from [JSONPlaceholder](https://jsonplaceholder.typicode.com/) to retrieve posts and comments.
- **Data Manipulation**: Processes and formats the data according to specific requirements.
- **CRUD-like Operations**: Provides endpoints to retrieve posts, comments, and detailed user posts with associated comments.

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/external-api-integration.git
cd external-api-integration
```

### Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```bash
pip install fastapi uvicorn requests
```

### Run the application:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading, so the server will restart whenever you make changes to the code.

## Usage

Once the server is running, you can access the API at `http://127.0.0.1:8000`.

## Endpoints

### 1. GET `/posts/`

**Description**: Retrieve all posts or a specific post by `postId`.

**Query Parameter:**

- `postId` (optional): The ID of the post to retrieve.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/posts/"
```

or

```bash
curl -X GET "http://127.0.0.1:8000/posts/?postId=1"
```

**Example Response:**

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
]
```

### 2. GET `/comments/`

**Description**: Retrieve all comments or comments for a specific post by `postId`.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/comments/?postId=1"
```

**Example Response:**

```json
[
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  }
]
```

### 3. GET `/formatted_posts/{userID}`

**Description**: Retrieve posts for a specific user and format the data.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/formatted_posts/1"
```

**Example Response:**

```json
{
  "userID": 1,
  "posts": [
    {
      "post_title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "post_body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
  ]
}
```

### 4. GET `/formatted_comment/{postID}`

**Description**: Retrieve comments for a specific post and format the data.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/formatted_comment/1"
```

**Example Response:**

```json
{
  "post_id": 1,
  "comments": [
    {
      "commenter_email": "Eliseo@gardner.biz",
      "commenter_name": "id labore ex et quam laborum",
      "comment": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }
  ]
}
```

### 5. GET `/detailed_post/{userID}`

**Description**: Retrieve all posts for a specific user along with their associated comments.

**Example Request:**

```bash
curl -X GET "http://127.0.0.1:8000/detailed_post/1"
```

**Example Response:**

```json
{
  "userID": 1,
  "posts": [
    {
      "post_title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
      "post_body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
      "comments": [
        {
          "commenter_name": "id labore ex et quam laborum",
          "commenter_email": "Eliseo@gardner.biz",
          "comment_body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
        }
      ]
    }
  ]
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- **Sir Paulo** for the idea!
- **FastAPI** for providing an easy-to-use and high-performance web framework.
- **JSONPlaceholder** for providing a free fake API for testing and prototyping.
- **Python** for being awesome.
