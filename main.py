from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/ping")
def get_ping():
    return JSONResponse(content="pong", status_code=200)