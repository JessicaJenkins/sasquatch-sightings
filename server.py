from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Sightings, User


app = Flask(__name__)

app.secret_key = "this-is-my-bigfoot"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Shows signup form for user"""
    return render_template("home.html")


@app.route("/register", methods=['POST'])
def register_process():
    """"""

    email = request.form["email"]
    password = request.form["password"]

    new_user = User()


@app.route("/map")
def display_map():
    return render_template("map.html")


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


@app.route("/sighting/<sighting_id>")
def show_event_details(sighting_id):
    
    sighting = Sightings.query.get(sighting_id)

    return render_template("sighting.html", sighting=sighting)


if __name__ == "__main__":
    app.debug = True
    
    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")