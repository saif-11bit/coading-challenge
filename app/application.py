from fastapi import FastAPI
import databases
import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

DB_URI=os.environ["DB_URI"]

app = FastAPI(title="Coading Challenge")

database = databases.Database(DB_URI, min_size=1, max_size=6)
metadata = sqlalchemy.MetaData()