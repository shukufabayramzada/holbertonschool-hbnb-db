import uuid
from datetime import datetime


class BaseClass:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()
