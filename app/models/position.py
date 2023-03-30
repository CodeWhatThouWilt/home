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
    user = db.relationship('User', back_populates='positions')
    # Position belongs to FuturesContract
    futures_contract = db.relationship('FuturesContract', back_populates='positions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'contractId': self.contract_id,
            'quantity': self.quantity,
            'status': self.status,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }