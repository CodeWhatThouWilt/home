from .db import db
from .mixins import TimestampMixin

class FuturesContract(db.Model, TimestampMixin):
    __tablename__ = 'futures_contracts'
    
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, unique=True, nullable=False)
    exchange = db.Column(db.String, nullable=False)
    contract_size = db.Column(db.Integer, nullable=False)
    tick_size = db.Column(db.Float, nullable=False)
    initial_margin = db.Column(db.Float, nullable=False)
    maintenance_margin = db.Column(db.Float, nullable=False)

    # One futures contract has many Orders
    orders = db.relationship('Order', back_populates='futures_contract')
    # One futures contract has many Trades
    trades = db.relationship('Trade', back_populates='futures_contract')
    # One futures contract many Positions
    positions = db.relationship('Position', back_populates='futures_contract')
    # One futures contract has many WatchlistItems
    watchlist_items = db.relationship('WatchlistItem', back_populates='futures_contract')
    # One futures contract has many historical prices
    historical_prices = db.relationship('HistoricalPrices', back_populates='futures_contract')
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'exchange': self.exchange,
            'contractSize': self.contract_size,
            'tickSize': self.tick_size,
            'initialMargin': self.initial_margin,
            'maintenanceMargin': self.maintenance_margin,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }