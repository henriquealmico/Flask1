from .extensions import db

class BaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()