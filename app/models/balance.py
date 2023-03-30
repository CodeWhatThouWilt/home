from .db import db
from .mixins import TimestampMixin


class Balance(db.Model, TimestampMixin):
    __tablename__ = 'balances'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0)

    user = db.relationship('User', back_populates='balance')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'balance': self.balance
        }
