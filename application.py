import os

from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from forms import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    if 'username' in session:
        return render_template('home.html')
    return redirect(url_for("index.html"))

@app.route("/sign_in", methods=['GET','POST'])
def sign_in():
    if 'username' in session:
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(name=form.username.data,password=form.password.data).first()
        if user:
            session['logged_in'] = True
            return redirect(url_for('home'))
        flash('Credentials invalid')
    return render_template('sign_in.html',form=form)

@app.route("/sign_up", methods=['GET','POST'])
def sign_up():
    if 'username' in session:
        return redirect(url_for('home'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit();
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('sign_up.html',form=form)

@app.route("/sign_out", methods=['GET','POST'])
@login_required
def sign_out():
    if 'username' in session:
        session.pop('logged_in',None)
    return render_template('index.html')




















    return render_template("sign_up.html")
