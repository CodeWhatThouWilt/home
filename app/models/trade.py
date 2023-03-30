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
    # Trade belongs to FuturesContract
    