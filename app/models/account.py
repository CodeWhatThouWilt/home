from .db import db
from .mixins import TimestampMixin

class Account(db.Model, TimestampMixin):
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    leverage = db.Column(db.Float, nullable=False)
    
    # Account belongs to one User
    user = db.relationship('User', back_populates='account', uselist=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'leverage': self.leverage,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }