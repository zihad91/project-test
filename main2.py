from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/message")
def massage():
    return {"message": "Fuck you"}
