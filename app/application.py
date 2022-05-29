import sys
import pathlib
sys.path.extend([str(pathlib.Path(__file__).parent.parent.absolute())])
from fastapi import FastAPI
import databases
import sqlalchemy
from dotenv import load_dotenv
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

load_dotenv(verbose=True)

DB_URI=os.environ["DB_URI"]

app = FastAPI(title="Coading Challenge")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


database = databases.Database(DB_URI, min_size=1, max_size=6)
metadata = sqlalchemy.MetaData()