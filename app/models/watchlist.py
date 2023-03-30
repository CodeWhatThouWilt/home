from .db import db
from .mixins import TimestampMixin

class Watchlist(db.Model, TimestampMixin):
    __tablename__ = 'watchlists'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    name = db.Column(db.String(20), nullable=False)
    
    user = db.relationship('User', back_populates='watchlists')
    watchlist_items = db.relationship('WatchlistItem', back_populates='watchlist')
    
    