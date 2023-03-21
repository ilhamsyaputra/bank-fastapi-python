from fastapi import FastAPI
from routers import nasabahRouter


app = FastAPI()

app.include_router(nasabahRouter.routes)