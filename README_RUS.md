# FADE - барбершоп

Сайт-визитка для барбершопа. Три статичные страницы, выполненные с акцентом на чистоту стилей и структуру кода.

## Стек технологий

- **HTML5** – семантическая разметка
- **CSS3** – кастомные стили, флексбоксы/гриды, адаптив

## Архитектура проекта

```
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

## Запуск

Достаточно открыть любой `.html` файл из папки `src/html/` в браузере.

## Особенности

- Чистый фронтенд без фреймворков
- Логичная файловая организация
- Готов к портированию на любой бэкенд

---

*Учебный проект.*
