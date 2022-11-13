from fastapi import FastAPI
from app.api.v1 import api
from app.core.config import settings

app = FastAPI()

for route in api.api_router.routes:
    if route.path.endswith('/'):  # type: ignore
        route.path = route.path[:-1]  # type: ignore

@app.get('/')
def index():
    return settings.APP_RUNNING


app.include_router(api.api_router, prefix=settings.BASE_URL_PREFIX)