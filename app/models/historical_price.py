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
    volumne = db.Column(db.Integer, nullable=False)
    
    # HistoricalPrice belongs to FuturesContract