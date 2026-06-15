"""
Заполнение базы данных тестовыми данными.
Запуск: ```docker compose exec backend python seed.py```
но только, если контейнер bakend пооднят! 
"""
"""
Заполнение базы данных тестовыми данными.
Запуск: docker compose exec backend python seed.py
"""

from app.core.database import SessionLocal
from app.models.user_model import User
from app.models.service_model import Service
from app.models.master_model import Master
from app.models.appointment_model import Appointment
from app.models.score_model import Score
from app.services.auth_service import get_password_hash
from datetime import datetime, timedelta
import random

def seed():
    db = SessionLocal()
    
    # 1. Создать админа и обычного пользователя, если их нет
    admin = db.query(User).filter(User.username == "admin").first()
    if not admin:
        admin = User(
            username="admin",
            email="admin@barbershop.com",
            password_hash=get_password_hash("admin123"),
            role="admin",
            created_at=datetime.utcnow()
        )
        db.add(admin)
    
    user = db.query(User).filter(User.username == "john_doe").first()
    if not user:
        user = User(
            username="john_doe",
            email="john@example.com",
            password_hash=get_password_hash("password123"),
            role="user",
            created_at=datetime.utcnow()
        )
        db.add(user)
    
    db.commit()
    print("✓ Пользователи добавлены")
    
    # 2. Услуги
    services_data = [
        {"services_name": "Стрижка", "duration_minutes": 30, "price": 1000, "description": "Классическая стрижка"},
        {"services_name": "Бритьё", "duration_minutes": 20, "price": 800, "description": "Бритьё опасной бритвой"},
        {"services_name": "Укладка", "duration_minutes": 25, "price": 700, "description": "Укладка воском/гелем"},
        {"services_name": "Стрижка + борода", "duration_minutes": 50, "price": 1600, "description": "Комплекс"},
    ]
    for s in services_data:
        if not db.query(Service).filter(Service.services_name == s["services_name"]).first():
            db.add(Service(**s))
    db.commit()
    print("✓ Услуги добавлены")
    
    # 3. Мастера
    masters_data = [
        {"name": "Иван Петров", "phone": "+79991234567", "status": "works"},
        {"name": "Алексей Смирнов", "phone": "+79997654321", "status": "works"},
        {"name": "Дмитрий Иванов", "phone": "+79998887777", "status": "on_vacation"},
    ]
    for m in masters_data:
        if not db.query(Master).filter(Master.name == m["name"]).first():
            db.add(Master(**m))
    db.commit()
    print("✓ Мастера добавлены")
    
    # 4. Записи (appointments) – несколько примеров
    services = db.query(Service).all()
    masters = db.query(Master).filter(Master.status == "works").all()
    users = db.query(User).all()
    
    if not db.query(Appointment).first():
        for i in range(5):
            apt = Appointment(
                user_id=random.choice(users).id,
                master_id=random.choice(masters).id,
                service_id=random.choice(services).id,
                appointment_date=datetime.utcnow() + timedelta(days=i+1, hours=10),
                created_at=datetime.utcnow(),
                status="confirmed"
            )
            db.add(apt)
        db.commit()
        print("✓ Тестовые записи добавлены")
    
    # 5. Оценки мастерам (scores)
    if not db.query(Score).first():
        for master in masters:
            for user in users:
                score = Score(
                    score_of_master_id=master.id,
                    score_by_user_id=user.id,
                    rating=random.randint(4,5),
                    feedback_text="Отличная работа!"
                )
                db.add(score)
        db.commit()
        print("✓ Оценки добавлены")
    
    print("Seeding завершён успешно!")
    db.close()

if __name__ == "__main__":
    seed()
