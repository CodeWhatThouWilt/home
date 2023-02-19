from .db import db, SCHEMA, environment


class Balance(db.Model):
    __tablename__ = 'balances'
    
    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    balance = db.Column(db.Float, nullable=False, default=0)

    user = db.relationship('User', back_populates='balance')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'balance': self.balance
        }
