from .db import db
from .mixins import TimestampMixin

class Position(db.Model, TimestampMixin):
    __tablename__ = 'positions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forex_pair_id = db.Column(db.Integer, db.ForeignKey('forex_pairs.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    
    # Position belongs to User
    user = db.relationship('User', back_populates='positions')
    # Position belongs to ForexPair
    futures_contract = db.relationship('ForexPair', back_populates='positions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'forexPairId': self.forex_pair_id,
            'quantity': self.quantity,
            'status': self.status,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }