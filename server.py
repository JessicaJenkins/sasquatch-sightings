from jinja2 import StrictUndefined

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db 


app = Flask(__name__)

app.secret_key = "this-is-my-bigfoot"
# app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
    return 'Hello, World!'


if __name__ == "__main__":
    
    app.debug = True
    
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")