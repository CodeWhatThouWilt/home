from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='demo', email='demo@aa.io', password='password',
        first_name='demo', last_name='user'
        )
    yake = User(
        username='yake', email='yake@aa.io', password='password',
        first_name='yake', last_name='dev'
        )
    dev = User(
        username='dev', email='dev@aa.io', password='password',
        first_name='dev', last_name='account'
        )

    db.session.add(demo)
    db.session.add(yake)
    db.session.add(dev)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()