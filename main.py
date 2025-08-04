from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.admin.auth_router import router as auth_router
from routes.user_router import router as user_router
from routes.setup_router import router as setup_router

# from routes.admin.router import router as admin_router
# from routes.admin.pmt_router import router as pmt_router
# from routes.member import router as member_router
from utils.file_uploader import *
import logging
import dotenv

dotenv.load_dotenv()

import strawberry
from strawberry.fastapi import GraphQLRouter

log_level = logging.INFO
if os.environ.get("DEBUG"):
    log_level = logging.DEBUG
print('DEBUG MODE', log_level)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(asctime)s | %(name)-15s | %(funcName)s() | L%(lineno)-2d | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log', mode='a'),
        # logging.FileHandler('app.log', mode='w')
    ]
)

logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI(
        title="NXTech Backend Service",
        description="Web-service For NXTech",
        version="1.0.0",
        prefix="/api/v1"
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()
app.include_router(user_router, prefix="/api/v1")
app.include_router(setup_router, prefix="/api/v1")
# app.include_router(admin_router, prefix="/api/v1")
# app.include_router(auth_router, prefix="/api/v1")
# app.include_router(pmt_router, prefix="/api/v1")

@app.get("/")
def index():
    return {"message": "NXTech backend is live"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
