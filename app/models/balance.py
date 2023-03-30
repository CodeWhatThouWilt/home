from .db import db
from .mixins import TimestampMixin


class Balance(db.Model, TimestampMixin):
    __tablename__ = 'balances'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0)

    # Balance belongs to one User
    user = db.relationship('User', back_populates='balance')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'balance': self.balance,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
