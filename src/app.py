# main flask file 
from flask import Flask, render_template
import requests

from database.db import connect_db


app = Flask(__name__)

connection = connect_db()
# обязательно поменять connect_db, нужно оспользовать пул соединений
# иначе для многопоточности не сгодится

from controller.home_controller import *
from controller.about_us_controller import *
from controller.appointment_controller import *


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
        )
