
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str

users_db = [
    {"user_id": 1, "name": "John Doe"},
    {"user_id": 2, "name": "Jane Smith"},
    {"user_id": 3, "name": "Alice Johnson"}
]

# GET 
@app.get("/users")
def read_users(user_id: Optional[int] = None):
    if user_id:  # Check if user_id is provided as a query parameter
        for user in users_db:
            if user["user_id"] == user_id:  # Return the user if found
                return {"status": "ok", "result": user}
        return {"error": "User not found"}  # Return error if user not found
    return {"status": "ok", "result": users_db}  # Return all users if no user_id is specified

# POST 
@app.post("/users")
def create_user(user: User):
    if any(existing_user['user_id'] == user.user_id for existing_user in users_db):
        return {"error": "User ID already exists"}  # Return error if user ID is already in use
    users_db.append(user.dict())  # Add the new user to the database
    return {"status": "ok", "result": user}

# PUT 
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(users_db):
        if existing_user["user_id"] == user_id:  # Check if user exists
            users_db[index]["name"] = user.name  # Update user details
            return {"status": "ok", "updated_data": users_db[index]}
    return {"error": "User not found. Cannot update record"}  # Return error if user not found

# DELETE 
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user["user_id"] == user_id:  # Check if user exists
            users_db.remove(user)  # Remove the user from the database
            return {"status": "ok", "removed_data": user}
    return {"error": "User not found. Cannot delete record"}  # Return error if user not found
