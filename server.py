#!/usr/bin/env python3
# HelpLine Bot (alpha release)

# import the serious stuff
from bottle import route, run
from pymongo import MongoClient


# receive the phone number
@route("/upload")
def upload():
    pass
    # do the stuff


# show a victim


# setup MongoDB
client = MongoClient()
database = client["helpline_db"]

# run the application
run(host="0.0.0.0", port = 8080, debug = True)