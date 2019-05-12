from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Sightings, User


app = Flask(__name__)

app.secret_key = "this-is-my-bigfoot"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():

    return render_template("map.html")

# @app.route("/home/<id>")
# def returns_home(id):


@app.route("/api/sightings")
def show_sightings():
    """JSON information about sightings"""
    sightings = Sightings.query.all()
    
    returned = [] 
    
    for sighting in sightings:
        if not sighting.lat:
            continue
        sightings_dict = {
            "sightingId": sighting.sighting_id,
            "userID": sighting.user_id,
            "sightingLat": sighting.lat,
            "sightingLng": sighting.lng,
            "sightingDate": sighting.date
            }

        returned.append(sightings_dict)

    return jsonify(returned)


@app.route("/event<event_id>")
def show_event_details(event_id):
    pass


if __name__ == "__main__":
    app.debug = True
    
    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")