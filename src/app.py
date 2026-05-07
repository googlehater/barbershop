# main flask file 
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


from controller.home_controller import *
from controller.about_us_controller import *
from controller.appointment_controller import *


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
        )
