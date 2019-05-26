from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import MetaData
import os

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

DB_SCHEMA = os.getenv('DB_SCHEMA_NAME', 'config')

from .user import User