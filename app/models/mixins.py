from .db import db
from datetime import datetime
from sqlalchemy.orm import declared_attr

class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)