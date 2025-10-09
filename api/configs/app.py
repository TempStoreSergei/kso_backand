from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket
from fastapi.security import HTTPBearer

from api.configs.middlewares import LoggingMiddleware
from modules.websocket.ws_manager import ws_manager
from scripts.drop_tables_db import drop_tables_db
from scripts.set_room_and_service import set_room_and_service
# from scripts.set_and_run_modules_services import set_and_run_modules_services
from scripts.set_users_db import set_users_db
from api.configs.loggers import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await drop_tables_db()
    await set_users_db()
    await set_room_and_service()
    # await set_and_run_modules_services()
    logger.info('Приложение запущено')
    yield
    logger.info('Приложение остановлено')


app = FastAPI(lifespan=lifespan)

app.add_middleware(LoggingMiddleware)


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws_manager.connect(ws)
    try:
        while True:
            message = await ws.receive_text()
            await ws_manager.broadcast(message)
    except Exception:
        ws_manager.disconnect(ws)

security = HTTPBearer()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
