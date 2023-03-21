from pydantic import BaseModel

class Transaksi(BaseModel):
    no_rekening: str
    nominal: int