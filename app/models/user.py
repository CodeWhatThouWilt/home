from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from .mixins import TimestampMixin


class User(db.Model, UserMixin, TimestampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

    # User has many Orders
    orders = db.relationship('Order', back_populates='user')
    # User has many Trades
    trades = db.relationship('Trade', back_populates='user')
    # User has many Positions
    positions = db.relationship('Position', back_populates='user')
    # User has many Watchlists
    watchlists = db.relationship('Watchlist', back_populates='user')
    # User has many Transactions
    transactions = db.relationship('Transaction', back_populates='user')
    # User has one Balance
    balance = db.relationship('Balance', back_populates='user', uselist=False)
    # User has one Account - future margin features etc
    # account = db.relationship('Account', back_populates='user', uselist=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at
        }
        
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    
