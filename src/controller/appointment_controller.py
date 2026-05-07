from flask import render_template
from app import app


@app.route("/appointment")
def appointment():
    return render_template("message.html")