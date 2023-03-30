from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from .mixins import TimestampMixin

class FururesContract(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String, unique=True, nullable=False)
    exchange = db.Column(db.String, nullable=False)
    contract_size = db.Column(db.Integer, nullable=False)
    tick_size = db.Column(db.Float, nullable=False)
    initial_margin = db.Column(db.Float, nullable=False)
    maintenance_margin = db.Column(db.Float, nullable=False)

    # One futures contract has many Orders
    # One futures contract has many Trades
    # One futures contract many Positions
    # One futures contract has many WatchlistItems
    # One futures contract has many historical prices