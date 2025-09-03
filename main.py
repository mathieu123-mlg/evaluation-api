from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/health")
def read_health():
    return "OK"


class Characteristic:
    ram_memory: int
    rom_memory: int

class PhoneModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic


phone_store: List[PhoneModel] = []

def serialized_stored_phones(phones=None):
    return [phones.model_dump() for phone in create_phones]

@app.post("/phones")
def create_phones(phone_lists: List[PhoneModel]):
    phone_store.extend(phone_lists)
    return JSONResponse(
        content={ "phone": serialized_stored_phones() },
        status_code=201
    )

@app.get("/phones")
def get_phones():
    return JSONResponse(
        content={ "phone": serialized_stored_phones() },
        status_code=200
    )

@app.get("/phones/{id}")
def get_phone_by_id():
    if id in serialized_stored_phones():
        result = phone_store.__contains__(id)
        return JSONResponse(content=result, status_code=200)
    return JSONResponse(content={"404": "Id Not Found"}, status_code=404)

@app.put("/phones/{id}/characteristics")
def set_characteristic_phone(characteristics: List[Characteristic]):
    return JSONResponse(content=characteristics, status_code=204)