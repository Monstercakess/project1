import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/home",)
def index():
    return render_template("home.html")

@app.route("/sign_in", methods=['POST','GET'])
def sign_in():
    if request.method == 'POST':
        return "not implemented"
    else:
        return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")
