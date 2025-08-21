from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/message")
def massage():
    return {"message": "Hello, this is a message from the FastAPI app!"}
