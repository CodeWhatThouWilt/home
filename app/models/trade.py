from .db import db
from .mixins import TimestampMixin

class Trade(db.Model, TimestampMixin):
    __tablename__ = 'trades'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey('futures_contracts.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    trade_type = db.Column(db.String, nullable=False)
    
    # Trade belongs to User
    user = db.relationship('User', back_populates='trades')
    # Trade belongs to FuturesContract
    futures_contract = db.relationship('FuturesContract', back_populates='trades')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'contractId': self.contract_id,
            'quantity': self.quantity,
            'price': self.price,
            'tradeType': self.trade_type,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    