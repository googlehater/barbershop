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

```
docker compose exec backend alembic upgrade head
```


```
docker compose exec backend python seed.py
```

```

```


## Features

- MVC architecture
- PostgreSQL database
- ORM will be added later

---

*Educational project.*

```
LP
├─ backend
│  ├─ alembic
│  │  ├─ alembic.ini
│  │  └─ migrations
│  ├─ app
│  │  ├─ api
│  │  ├─ core
│  │  ├─ main.py
│  │  ├─ models
│  │  ├─ schemas
│  │  └─ services
│  ├─ Dockerfile
│  └─ requirements.txt
├─ docker-compose.yaml
├─ docs
│  ├─ Otchet_Ryzhov_23-II_1.pdf
│  ├─ ryzhov_otchet_II.pdf
│  ├─ Задание к лабе 1.txt
│  ├─ Задание к лабе 2.txt
│  └─ Задание к лабе 3.txt
├─ frontend
│  ├─ Dockerfile
│  ├─ package.json
│  └─ src
│     ├─ App.jsx
│     ├─ components
│     ├─ pages
│     └─ services
├─ README.md
├─ README_RUS.md
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
   │     ├─ barbershop_Interior.jpg
   │     ├─ barbershop_vibe.jpg
   │     ├─ Beard_care.jpg
   │     ├─ haircut_1.jpg
   │     ├─ haircut_2.jpg
   │     ├─ haircut_3.jpg
   │     ├─ like_a_model_cut.jpeg
   │     ├─ Shaving_with_a_straight_razor.png
   │     └─ tape_1.jpg
   └─ templates
      ├─ about_us.html
      ├─ index.html
      └─ message.html

```