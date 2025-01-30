from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def calculate_factorial(starting_number: int):
    if starting_number == 0:
        return {"result": False}
    
    result = 1
    current_number = starting_number
    
    while current_number > 1:
        result *= current_number
        current_number -= 1
    
    return {"result": result}

#http://127.0.0.1:8000/factorial/{your number here}