import uuid
from datetime import datetime
from app import db

class BaseClass(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()
