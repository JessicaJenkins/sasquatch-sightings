import datetime
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request, flash, redirect, session, Markup
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Sightings, User


app = Flask(__name__)

app.secret_key = "this-is-my-bigfoot"
app.jinja_env.undefined = StrictUndefined


@app.route("/register")
def register_form():
    """Shows signup form for new user"""
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_process():
    """Allows new user to register"""

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    existing_user = User.query.filter_by(email=email).first()

    new_user = User(name=name, email=email, password=password)

    if new_user.email == existing_user.email:
        flash("This email address is already in use.")
        return redirect("/register")
    else:
        db.session.add(new_user)
        db.session.commit()

        flash("Thanks for signing up!")
        return redirect("/map")


@app.route("/login")
def display_login_form():
    """Shows existing user login form"""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def log_in_user():
    """Signs in existing user, or prompts them to sign up."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No account found with that email address.")
        return redirect("/login")

    if user.password != password:
        flash("Password incorrect")
        return redirect("/login")

    session["user_id"] = user.user_id

    return redirect("/map")


@app.route("/map")
def display_map():
    """Displays Google Map with markers."""

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
            "sightingDate": sighting.date.strftime("%A, %b %d, %Y")
            }

        returned.append(sightings_dict)

    return jsonify(returned)


@app.route("/add_sighting")
def show_new_sighting_form():
    """Displays form to add a new sighting"""
    
    return render_template("add_sighting.html")


@app.route("/add_sighting", methods=["POST"])
def add_new_sighting():
    """Gives registered users the ability to add a new sighting."""

    date = request.form.get("date")
    date = datetime.datetime.strptime(date, "%m/%d/%Y").date()

    description = request.form.get("description")

    new_sighting = Sightings(date=date, description=description)

    return redirect("/")



@app.route("/sighting/<sighting_id>")
def show_event_details(sighting_id):
    
    sighting = Sightings.query.get(sighting_id)

    return render_template("sighting.html", sighting=sighting)


if __name__ == "__main__":
    app.debug = True
    
    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")