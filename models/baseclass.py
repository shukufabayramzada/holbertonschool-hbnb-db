import uuid
from datetime import datetime
from database import db

class BaseClass(db.Model):
    __abstract__ = True
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()