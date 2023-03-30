from .db import db
from .mixins import TimestampMixin

class WatchlistItem(db.Model, TimestampMixin):
    __tablename__ = 'watchlist_items'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'), nullable=True, index=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('futures_contracts.id'), nullable=True)
    
    # WatchlistItem belongs to watchlist
    watchlist = db.relationship('Watchlist', back_populates='watchlist_items')
    # WatchlistItem belongs to FuturesContract
    futures_contract = db.relationship('Contract', back_populates='watchlist_items')
    
    def to_dict(self):
        return {
            'id': self.id,
            'watchlistId': self.watchlist_id,
            'contactId': self.contract_id,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    