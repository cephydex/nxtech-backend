from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
import dotenv
# from routes.admin.auth_router import router as auth_router
from routes.user_router import router as user_router
from routes.setup_router import router as setup_router
from routes.func_router import router as func_router
from quote_admin.controller import router as admin_quote_router
from policy_admin.controller import router as admin_policy_router
from log_conf import init_logger
import strawberry
from strawberry.fastapi import GraphQLRouter


dotenv.load_dotenv()

init_logger()
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
app.include_router(func_router, prefix="/api/v1")
app.include_router(admin_quote_router, prefix="/api/v1")
app.include_router(admin_policy_router, prefix="/api/v1")

@app.get("/")
def index():
    return {"message": "NXTech backend is live"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
