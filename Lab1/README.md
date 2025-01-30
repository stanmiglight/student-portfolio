# Factorial Calculator API

This is a simple FastAPI-based web service that calculates the factorial of a given integer. The API provides an endpoint where you can send a number, and it will return the factorial of that number.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Factorial Calculation**: The API calculates the factorial of a given integer using a while loop.
- **Error Handling**: If the input number is 0, the API returns `{ "result": false }` since the factorial of 0 is not defined in this implementation.

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/factorial-api.git
cd factorial-api
```

### Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies:

```bash
pip install fastapi uvicorn
```

### Run the application:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading, so the server will restart whenever you make changes to the code.

## Usage

Once the server is running, you can access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Endpoint

`GET /factorial/{starting_number}`: Calculates the factorial of the provided integer.

#### Example Request:

```bash
curl -X GET "http://127.0.0.1:8000/factorial/5"
```

#### Example Response:

```json
{
  "result": 120
}
```

#### Example Request for 0:

```bash
curl -X GET "http://127.0.0.1:8000/factorial/0"
```

#### Example Response:

```json
{
  "result": false
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- **Sir Paulo** for the idea!
- **FastAPI** for providing an easy-to-use and high-performance web framework.
- **Python** for being awesome.
