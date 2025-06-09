# config/database.py
from masoniteorm.connections import ConnectionResolver
from masoniteorm.config import db_url
import os
import dotenv

dotenv.load_dotenv()

# DB_URL="postgresql://postgres:postgres@musiga-db/genit"
DB_URL = os.getenv("DATABASE_URL")
import dotenv

dotenv.load_dotenv()

# DB_URL="postgresql://postgres:postgres@musiga-db/genit"
DB_URL = os.getenv("DATABASE_URL")
# DB_URL = os.environ.get("DATABASE_URL")
# print("DB_URL", DB_URL)

DATABASES = {
  "default": "postgres",
  "mysql": {
    "host": "127.0.0.1",
    "driver": "mysql",
    "database": "masonite",
    "user": "root",
    "password": "",
    "port": 3306,
    "log_queries": False,
    "options": {
      #
    }
  },
  # "postgres": db_url(log_queries=False, prefix="", options={}),
  "postgres": db_url(DB_URL, log_queries=False, prefix="", options={}),
  "postgres2": {
    "host": "musiga-db",
    "driver": "postgres",
    "database": "genit",
    "user": "postgres",
    "password": "postgres",
    "port": 5432,
    "log_queries": False,
    "options": {
      #
    }
  },
  "sqlite": {
    "driver": "sqlite",
    "database": "masonite.sqlite3",
  }
}

DB = ConnectionResolver().set_connection_details(DATABASES)
