# FADE - барбершоп

Сайт-визитка для барбершопа. Три статичные страницы, выполненные с акцентом на чистоту стилей и структуру кода.

## Стек технологий

- Python 3
- Flask
- Jinja2
- PostgreSQL
- HTML5
- CSS3
- Docker
- Docker Compose

## Архитектура проекта

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

## Архитектура MVC

- **Model** (model/) — работа с базой данных и выполнение SQL-запросов.
- **View** (templates/) — HTML-шаблоны Jinja2.
- **Controller** (controller/) — обработка HTTP-запросов и координация работы приложения.

## База данных

Инициализация структуры БД выполняется автоматически с помощью файла 
```
src/database/init.sql
```

## Запуск

В корне пректа запустить командой:

```bash
docker compose up
```

После запуска приложение будет доступно оп андресу:
```
http://localhost:8080/
```


## Особенности

- Архитектура MVC
- База данных PostgreSQL
- Позже добавится ORM

---

*Учебный проект.*
