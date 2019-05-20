import os
import json

import pandas as pd
import numpy as np
import pymysql

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# engine = create_engine(
#     "mysql://rl91qzpzgty8oaf1:evamhxfd7l42mgso@y2w3wxldca8enczv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/v21ogkg4wvsne316")
#
# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
#
# # print table names
# print(engine.table_names())
# # Save reference to the table
# Hale = Base.classes.hale


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://rl91qzpzgty8oaf1:evamhxfd7l42mgso@y2w3wxldca8enczv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/v21ogkg4wvsne316"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Hale = Base.classes.hale
LexByCountry = Base.classes.lexbycountry
#
#


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/countries")
def names():
    """Return a list of countries."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(LexByCountry).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    df.head()
    # Return a list of the column names (sample names)
    return jsonify(list(df['Country'].unique()))


@app.route("/data")
def all_data():
    """Return all data."""
    stmt = db.session.query(LexByCountry).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    df['Year'] = df['Year'].astype(str)
    jsonfiles = json.loads(df.to_json(orient='records'))
    return jsonify(jsonfiles)


@app.route("/hales/<country>")
def hale(country):
    """Return the data for a given country."""
    sel = [
        Samples_Metadata.sample,
        Samples_Metadata.ETHNICITY,
        Samples_Metadata.GENDER,
        Samples_Metadata.AGE,
        Samples_Metadata.LOCATION,
        Samples_Metadata.BBTYPE,
        Samples_Metadata.WFREQ,
    ]

    results = db.session.query(
        *sel).filter(Samples_Metadata.sample == sample).all()

    print(results)
  # Create a dictionary entry for each row of metadata information
    sample_metadata = {}
    for result in results:
        sample_metadata["sample"] = result[0]
        sample_metadata["ETHNICITY"] = result[1]
        sample_metadata["GENDER"] = result[2]
        sample_metadata["AGE"] = result[3]
        sample_metadata["LOCATION"] = result[4]
        sample_metadata["BBTYPE"] = result[5]
        sample_metadata["WFREQ"] = result[6]

    return jsonify(sample_metadata)


@app.route("/lexs/<country>")
def samples(country):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    # Format the data to send as json
    data = {
        "otu_ids": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
