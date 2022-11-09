

# penser à installer pandas et numpy et flask
from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")
migrate = Migrate(app, db)

@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route("/choose-account")
def choose_account():
    return render_template('choose-account.html')

@app.route("/operations/")
def operations():
    return render_template("list-operations.html")