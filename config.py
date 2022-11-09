import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://scott:tiger@localhost/mydatabase' # uri connection
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ECHO = True  # If set to True SQLAlchemy will log all the statements issued to stderr which can be
# useful for debugging.


