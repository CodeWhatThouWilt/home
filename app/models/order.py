from .db import db
from .mixins import TimestampMixin

class Order(db.Model, TimestampMixin):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey('futures_contract.id'), nullable=False)
    order_type = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_status = db.Column(db.String, nullable=False)
    
    # Order belongs to FuturesContract
    # Order belongs to User