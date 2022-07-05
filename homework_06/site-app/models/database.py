import os
from flask_sqlalchemy import SQLAlchemy

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


db = SQLAlchemy()