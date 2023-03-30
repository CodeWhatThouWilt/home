from .db import db
from .mixins import TimestampMixin

class Watchlist(db.Model, TimestampMixin):
    __tablename__ = 'watchlists'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    name = db.Column(db.String(20), nullable=False)
    
    # Watchlist belongs to User
    user = db.relationship('User', back_populates='watchlists')
    # Watchlist has many WatchlistItems
    watchlist_items = db.relationship('WatchlistItem', back_populates='watchlist')
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'name': self.name,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
    