from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class Nasabah(BaseModel):
    nama: str
    nik: str
    no_hp: str