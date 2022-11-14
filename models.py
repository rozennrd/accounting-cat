from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


import datetime
from app import db


from flask_login import LoginManager
login = LoginManager()
 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
 
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)
    name = db.Column(db.String(30))

    # Operations in operation > backref.

    def add_operation(self, operation):
        self.balance += operation.amount
        self.operations.append(operation)

    def show_balance(self):
        print(self.name, " : ", self.balance)

    def list_operations(self):
        for operation in self.operations:
            operation.show()

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    reason = db.Column(db.String(120))
    date = db.Column(db.DateTime, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    account = db.relationship('Account',
                               backref=db.backref('operations', lazy=True))

    def __init__(self, amount, reason=None, date=datetime.date.today(), category="défaut"):
        self.amount = amount
        self.reason = reason
        self.date = date
        self.category = category

    def show(self):
        print(self.date, "\t", self.reason, "\t", self.category, "\t", self.amount)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def get_name(self):
        return self.name

    def __repr__(self):
        return '<Category %r>' % self.name
