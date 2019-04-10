from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

class = User(db.Model):
    """User of the Sasquatch Sightings website"""

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    email = db.Column(db.String(100), nullable=False)



class = Sightings(db.Model):

    sighting_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    lat = db.Column(db.Integer(100))