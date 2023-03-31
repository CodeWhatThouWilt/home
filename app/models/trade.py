from .db import db
from .mixins import TimestampMixin

class Trade(db.Model, TimestampMixin):
    __tablename__ = 'trades'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forex_pair_id = db.Column(db.Integer, db.ForeignKey('forex_pairs.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    trade_type = db.Column(db.String, nullable=False)
    
    # Trade belongs to User
    user = db.relationship('User', back_populates='trades')
    # Trade belongs to ForexPair
    forex_pair = db.relationship('ForexPair', back_populates='trades')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'forexPairId': self.forex_pair_id,
            'quantity': self.quantity,
            'price': self.price,
            'tradeType': self.trade_type,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    