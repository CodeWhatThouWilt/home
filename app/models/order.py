from .db import db
from .mixins import TimestampMixin

class Order(db.Model, TimestampMixin):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forex_pair_id = db.Column(db.Integer, db.ForeignKey('forex_pairs.id'), nullable=False)
    order_type = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_status = db.Column(db.String, nullable=False)
    
    # Order belongs to ForexPair
    forex_pair = db.relationship('ForexPair', back_populates='orders')
    # Order belongs to User
    user = db.relationship('User', back_populates='orders')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'forexPairId': self.forex_pair_id,
            'orderType': self.order_type,
            'quantity': self.quantity,
            'price': self.price,
            'orderStatus': self.order_status,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }