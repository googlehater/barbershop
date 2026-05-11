from flask import render_template, request, redirect, url_for
from app import app, connection
from model.services_model import service_model

from model.services_model import service_model
from model.appointment_model import AppointmentModel

appointment_model = AppointmentModel(connection)

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    print("appointment route called")
    print(f'request method: {request.method}')

    if request.method == "POST":
        print(f"POST data: {request.form}")
        name = request.form.get("name", "").strip()  # удаляем лишние пробелы
        phone = request.form.get("phone", "").strip()
        service_id = request.form.get("service", "").strip()
        date = request.form.get("date")
        time = request.form.get("time")
        comment = request.form.get("comment", "").strip()
        master_id = request.form.get("master") or 1

        if not name:
            return "Name is required", 400
        
        if len(phone) < 10:
            return "phone is too short", 400
        
        if len(phone) > 50:
            return "phone is too long", 400

        if len(name) > 100:
            return "name is too long", 400
        
        if not service_id or not service_id.isdigit():
            return "please select a valid service", 400
        service_id = int(service_id)  
        
        appointment_datetime = f"{date} {time}:00"

        appointment_model.create_appointment(
            client_name=name,
            phone=phone,
            service_id=service_id,
            appointment_datetime=appointment_datetime,
            client_wish=comment,
            master_id=int(master_id) if str(master_id).isdigit() else 1
        )

        
        return redirect(url_for("appointment"))

    services = service_model.get_all_services()
    return render_template("message.html", services=services)
