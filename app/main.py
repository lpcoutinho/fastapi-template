"""Main FastAPI app instance declaration."""

from fastapi import FastAPI

from app.core import config

app = FastAPI(
    title=config.settings.PROJECT_NAME,
    version=config.settings.VERSION,
    description=config.settings.DESCRIPTION,
    openapi_url="/openapi.json",
    docs_url="/",
)

@app.get('/healthcheck')
def healthcheck():
    return "Hello World"