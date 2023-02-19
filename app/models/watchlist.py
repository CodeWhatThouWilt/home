from .db import db, SCHEMA, environment

class Watchlist(db.Model):
    __tablename__ = 'watchlists'
    
    if environment == 'production':
        __table_args__ = { 'schema': SCHEMA }
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.Datetime, default=db.func.now())
    
    user = db.relationship('User', back_populates='watchlists')
    watchlist_items = db.relationship('WatchlistItem', back_populates='watchlist')
    
    