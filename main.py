from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Vistona backend is running 🚀"}

@app.get("/age/{age}")
def increase_age(age: int):
    new_age = age + 1
    return {"old_age": age, "new_age": new_age}