from fastapi import FastAPI
from routers import nasabahRouter, transaksiRouter, saldoRouter, mutasiRouter


app = FastAPI()

app.include_router(nasabahRouter.routes)
app.include_router(transaksiRouter.routes)
app.include_router(saldoRouter.routes)
app.include_router(mutasiRouter.routes)