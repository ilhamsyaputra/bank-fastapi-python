from fastapi import FastAPI
from routers import nasabahRouter, transaksiRouter


app = FastAPI()

app.include_router(nasabahRouter.routes)
app.include_router(transaksiRouter.routes)