from pydantic import BaseModel

class Nasabah(BaseModel):
    nama: str
    nik: str
    no_hp: str