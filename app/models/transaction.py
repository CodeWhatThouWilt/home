from .db import db, SCHEMA, environment

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }
        
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False) # DEPOSIT OR WITHDRAW
    amount = db.Column(db.Float, nullable =False)
    
    user = db.relationship('User', back_populates='transactions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'transactionType': self.transaction_type,
            'amount': self.amount
        }