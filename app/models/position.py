from .db import db
from .mixins import TimestampMixin

class Position(db.Model, TimestampMixin):
    __tablename__ = 'positions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    contract_id = db.Column(db.Intefer, db.ForeignKey('futures_contracts.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    
    # Position belongs to User
    # Position belongs to FuturesContract