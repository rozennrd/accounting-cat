

# penser à installer pandas et numpy et flask
from distutils.log import Log
from flask import Flask, request, render_template, redirect
from flask_login import current_user, login_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from forms import SignUpForm, LoginForm
from models import User


db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")
migrate = Migrate(app, db)

# A supprimer quand on utilisera python-dotenv. 
# Pour l'instant, je veux arriver à gérer le login d'abord. 
from config import SECRET_KEY
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/login')
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect('/blogs')
     
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/blogs')
     
    return render_template('login.html', form = form)


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)


@app.route("/choose-account")
def choose_account():
    return render_template('choose-account.html')


@app.route("/operations/")
def operations():
    return render_template("list-operations.html")