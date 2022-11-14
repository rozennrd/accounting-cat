

# penser à installer pandas et numpy et flask
from distutils.log import Log
from flask import Flask, request, render_template, redirect, flash
from flask_login import current_user, login_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from forms import SignUpForm, LoginForm

import config


app = Flask(__name__, template_folder="templates")

app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

# Importing models after db and app creation, to avoid circular imports problems. 
from models import User
# A supprimer quand on utilisera python-dotenv. 
# Pour l'instant, je veux arriver à gérer le login d'abord. 

#app.config['SECRET_KEY'] = config.SECRET_KEY


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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        passwd=form.password.data 
        confirm = form.confirm_password.data
        print(passwd, confirm, passwd == confirm)
        if passwd != confirm:
            flash("Erreur : les deux mots de passe doivent être identiques")
        else : 
            user = User(email=form.username.data)
            user.password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Vous êtes bien enregistré")
    return render_template('signup.html', form=form)


@app.route("/choose-account")
def choose_account():
    return render_template('choose-account.html')


@app.route("/operations/")
def operations():
    return render_template("list-operations.html")