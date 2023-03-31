from .db import db
from .mixins import TimestampMixin

class WatchlistItem(db.Model, TimestampMixin):
    __tablename__ = 'watchlist_items'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'), nullable=True, index=True)
    forex_pair_id = db.Column(db.Integer, db.ForeignKey('forex_pairs.id'), nullable=True)
    
    # WatchlistItem belongs to watchlist
    watchlist = db.relationship('Watchlist', back_populates='watchlist_items')
    # WatchlistItem belongs to ForexPair
    forex_pair = db.relationship('ForexPair', back_populates='watchlist_items')
    
    def to_dict(self):
        return {
            'id': self.id,
            'watchlistId': self.watchlist_id,
            'forexPairId': self.forex_pair_id,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    