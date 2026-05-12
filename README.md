# FADE – Barber Shop

A business card website for a barber shop. Three static pages, built with a focus on clean styling and code structure.

## Tech Stack

- Python 3
- Flask
- Jinja2
- PostgreSQL
- HTML5
- CSS3
- Docker
- Docker Compose

## Project Architecture

```text
Fade
├─ docker-compose.yaml
├─ Dockerfile
├─ docs
│  ├─ Otchet_Ryzhov_23-II_1.pdf
│  ├─ Задание к лабе 1.txt
│  └─ Задание к лабе 2.txt
├─ README.md
├─ README_RUS.md
├─ requirements.txt
└─ src
   ├─ app.py
   ├─ controller
   │  ├─ about_us_controller.py
   │  ├─ appointment_controller.py
   │  └─ home_controller.py
   ├─ database
   │  ├─ db.py
   │  └─ init.sql
   ├─ model
   │  ├─ appointment_model.py
   │  ├─ services_model.py
   │  └─ __init__.py
   ├─ static
   │  ├─ css
   │  │  └─ style.css
   │  └─ img
   └─ templates
      ├─ about_us.html
      ├─ index.html
      └─ message.html
```

## MVC Architecture
- **Model** (model/) — database interaction and execution of SQL queries.
- **View** (templates/) — Jinja2 HTML templates.
- **Controller** (controller/) — handling HTTP requests and coordinating the application.

## Database

The database schema is initialized automatically using the following file:

```
src/database/init.sql
```

## How to Run

Run the following command in the project root directory:
```bash
docker compose up
```

After startup, the application will be available at:
```
http://localhost:8080/
```

## Features

- MVC architecture
- PostgreSQL database
- ORM will be added later

---

*Educational project.*
