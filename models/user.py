from models import db, DB_SCHEMA
from sqlalchemy.dialects import postgresql
from sqlalchemy.types import JSON


class User(db.Model):
    __table_args__ = {"schema": DB_SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    dob = db.Column(db.Date())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

