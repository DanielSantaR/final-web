import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.db import init_db

from .debugger import initialize_fastapi_server_debugger_if_needed

log = logging.getLogger("uvicorn.error")


def create_application() -> FastAPI:
    initialize_fastapi_server_debugger_if_needed()
    application = FastAPI()
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
