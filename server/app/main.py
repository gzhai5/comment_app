import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from loguru import logger
from app.utils.database import test_mongodb_connection
from app.comment.comment_router import router as comment_router


# Create the app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    test_mongodb_connection()
    logger.info("INFO: App started successfully")

    yield

    # shutdown logic
    logger.info("INFO: App stopped successfully")
app = FastAPI(title="BackEnd Server", lifespan=lifespan)


# set the CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # allow the cookie
    allow_methods=["*"],  # allow all http methods
    allow_headers=["*"],  # all all headers
)


# include the routers
app.include_router(comment_router)


# Home route
@app.get("/")
async def home():
    return {"message": "This is the back-end Server"}


# Exception handler
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )