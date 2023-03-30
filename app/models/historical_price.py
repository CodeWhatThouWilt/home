from .db import db
from .mixins import TimestampMixin

class HistoricalPrice(db.Model, TimestampMixin):
    __tablename__ = 'historical_prices'
    
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('futures_contracts.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    
    # HistoricalPrice belongs to FuturesContract
    futures_contract = db.relationship('FuturesContract', back_populates='historical_prices')
    
    def to_dict(self):
        return {
            'id': self.id,
            'contractId': self.contract_id,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volumne': self.volume,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }