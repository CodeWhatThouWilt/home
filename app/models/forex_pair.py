from .db import db
from .mixins import TimestampMixin

class ForexPair(db.Model, TimestampMixin):
    __tablename__ = 'forex_pairs'
    
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, unique=True, nullable=False)
    base_currency = db.Column(db.String, nullable=False)
    quote_currency = db.Column(db.String, nullable=False)
    initial_margin = db.Column(db.Float, nullable=False)
    maintenance_margin = db.Column(db.Float, nullable=False)

    # One ForexPair has many Orders
    orders = db.relationship('Order', back_populates='forex_pair')
    # One ForexPair has many Trades
    trades = db.relationship('Trade', back_populates='forex_pair')
    # One ForexPair many Positions
    positions = db.relationship('Position', back_populates='forex_pair')
    # One ForexPair has many WatchlistItems
    watchlist_items = db.relationship('WatchlistItem', back_populates='forex_pair')
    # One ForexPair has many historical prices
    historical_prices = db.relationship('HistoricalPrices', back_populates='forex_pair')
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'baseCurrency': self.base_currency,
            'quoteCurrency': self.quote_currency,
            'initialMargin': self.initial_margin,
            'maintenanceMargin': self.maintenance_margin,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }