from flask import render_template
from app import app
from model.services_model import service_model


@app.route("/appointment")
def appointment():
    services = service_model.get_all_services()
    return render_template("message.html", services=services)
