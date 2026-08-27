import fastapi
from fastapi import FastAPI, Response

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}