from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/message")
def massage():
    return {"message": "এ Mottaleb, my first app is dedicated to you!"}
