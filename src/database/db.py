# connect to db 
import psycopg2
import os
import time


def connect_db(retries=5, delay=2):
    # обязательно поменять connect_db, нужно оспользовать пул соединений
    # иначе для многопоточности не сгодится
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                database=os.getenv('DB_NAME', 'postgres'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', 'postgres')
            )
            print("database connection successful")
            return conn
        except Exception as e:
            if attempt < retries - 1:
                print(f"database connection failed (attempt {attempt + 1}/{retries}). Retrying in {delay} seconds...")
                time.sleep(delay)
            
            print(f"error connecting to the database: {e}")
            return None