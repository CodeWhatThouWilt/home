from .db import db
from .mixins import TimestampMixin

class HistoricalPrice(db.Model, TimestampMixin):
    __tablename__ = 'historical_prices'
    
    id = db.Column(db.Integer, primary_key=True)
    forex_pair_id = db.Column(db.Integer, db.ForeignKey('forex_pairs.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    
    # HistoricalPrice belongs to ForexPair
    forex_pair = db.relationship('ForexPair', back_populates='historical_prices')
    
    def to_dict(self):
        return {
            'id': self.id,
            'forexPairId': self.forex_pair_id,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volumne': self.volume,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }