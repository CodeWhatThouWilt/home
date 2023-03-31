from flask import Blueprint, jsonify, request
from flask_login import login_required
import requests
import os

API_KEY = os.environ.get('ALPHA_VANTAGE_API')

forex_pairs_routes = Blueprint('forexpairs', __name__)

@forex_pairs_routes.route('/')
def get_pairs_data():
    symbol = request.args.get('symbol')
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    url = f'https://www.alphavantage.co/query?function=WTI&interval=daily&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data