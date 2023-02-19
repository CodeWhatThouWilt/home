from .db import db, SCHEMA, environment

class WatchlistItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'), nullable=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('futures_contracts.id'), nullable=True)
    
    user = db.relationship('User', back_populates='watchlist_items')
    watchlist = db.relationship('Watchlist', back_populates='watchlist_items')
    contract = db.relationship('Contract', back_populates='watchlist_items')
    