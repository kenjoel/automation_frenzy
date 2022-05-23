from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
from loguru import logger
from config import LOGDIR, LOGFILE, ORIGINS, BASEDIR

LOGDIR = BASEDIR + "/" + LOGDIR

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)

logger.add(LOGDIR + "/" + LOGFILE,
           rotation="10MB",
           colorize=True,
           format="<green>{time:YYYYMMDD_HH:mm:ss}</green> | <level>{message}</level>)",
           level="ERROR"
           )

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]

for i in ORIGINS.split(","):
    origins.append(i)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api import panda_magic
