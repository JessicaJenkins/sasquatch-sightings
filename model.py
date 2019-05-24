"""Model and database functions for the Sasquatch Sitings website"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User of the Sasquatch Sightings website"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Prints readable info about users"""

        return "user_id: {}, name: {}, email: {}".format(self.user_id,
            self.name,
            self.email)


class Sightings(db.Model):
    """A sighting recorded on the Sasquatch Sightings website"""

    __tablename__ = "sightings"

    sighting_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    lat = db.Column(db.String(2500))
    lng = db.Column(db.String(2500))
    date = db.Column(db.Date)
    event_desc = db.Column(db.Text)

    def __repr__(self):
        """Prints readable info about sightings without description"""

        return "ID: {}, user_id: {}, lat: {}, long: {}, date: {}".format(self.sighting_id,
            self.user_id,
            self.lat,
            self.lng,
            self.date)


def connect_to_db(app):
    """Connect the database to the Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sasquatch'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """Lets me interact with the database if run interactively"""

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
