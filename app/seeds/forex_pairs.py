from app.models import db, ForexPair, environment, SCHEMA
from .currency_data import currency_data

def seed_forex_pairs():
    for currency in currency_data:
        for other_currency in currency_data:
            if other_currency != currency:
                pair = ForexPair(
                    symbol=f"{currency['currency_code']}/{other_currency['currency_code']}",
                    base_currency=currency['currency_code'],
                    base_currency_name=currency['currency_name'],
                    quote_currency = other_currency['currency_code'],
                    quote_currency_name = other_currency['currency_name']
                )
                db.session.add(pair)
                
    db.session.commit()
    
def undo_forex_pairs():
    db.session.execute("DELETE FROM forex_pairs")     
    db.session.commit()