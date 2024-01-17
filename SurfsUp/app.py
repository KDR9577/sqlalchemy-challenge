# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()
# Save references to each table
#measurements = Base.classes.hawaii_measurements
#stations = Base.classes.hawaii_stations

# Create our session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)



#################################################
# Flask Routes
#################################################
#@app.route("/")
#def home():
    #print("Server received request for 'Home' page...")
    #return "Welcome to my home page"