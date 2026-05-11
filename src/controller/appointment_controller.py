from flask import render_template, request, redirect, url_for
from app import app
from model.services_model import service_model


@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        name = request.form.get("name", "").strip()  # удаляем лишние пробелы
        phone = request.form.get("phone", "").strip()
        comment = request.form.get("comment", "").strip()

        if not name:
            return "Name is required", 400
        
        if len(phone) < 10:
            return "phone is too short"
        
        if len(phone) > 16:
            return "phone is too long"

        if len(name) > 100:
            return "name is too long"
        
        return redirect(url_for("appointment"))

    services = service_model.get_all_services()
    return render_template("message.html", services=services)
