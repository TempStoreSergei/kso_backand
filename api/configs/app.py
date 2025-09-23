from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.security import HTTPBearer

from scripts.drop_tables_db import drop_tables_db
from scripts.set_and_run_modules_services import set_and_run_modules_services
from scripts.set_terminal_functions_db import set_terminal_functions_db
from scripts.set_user_functions_map_db import set_user_functions_map_db
from scripts.set_users_db import set_users_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    # await drop_tables_db()
    await set_users_db()
    await set_terminal_functions_db()
    await set_user_functions_map_db()
    await set_and_run_modules_services()

security = HTTPBearer()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
