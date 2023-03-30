from .db import db
from .mixins import TimestampMixin

class Transaction(db.Model, TimestampMixin):
    __tablename__ = 'transactions'
        
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False) # DEPOSIT OR WITHDRAW
    amount = db.Column(db.Float, nullable =False)
    
    # Transaction belongs to User
    user = db.relationship('User', back_populates='transactions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'transactionType': self.transaction_type,
            'amount': self.amount,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }