import psycopg2
from psycopg2.extras import RealDictCursor
# import sqlalchemy as sa
# at 2nd lab we should use sql only. no orm



# решил не делать остальные модели, тк птом все равно orm добавлять

class AppointmentModel:
    # ToDo: BaseModel for theese 2 funcs
    def __init__(self, db_connection_or_func):
        """
        get_connection_func - for psycopg2 connection
        """
        if callable(db_connection_or_func):
            self.get_conn = db_connection_or_func

        self.get_conn = lambda: db_connection_or_func

    def _execute(self, query, params=None, fetch=True, fetch_one=False, commit=True):
        """
        method for executing queries to the database
        """
        conn = self.get_conn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                if fetch:
                    if fetch_one:
                        return cursor.fetchone()
                    else:
                        return cursor.fetchall()
                else:
                    result = None
                conn.commit()
                return result
        except Exception as e:
            print(f'db error: {e}')
            conn.rollback()
            raise e

    def get_all_appointments(self):
        query = "SELECT * FROM appointments ORDER BY id"
        return self._execute(query)
    
    def get_by_id(self, id):
        query = "SELECT * FROM appointments WHERE id = %s"
        return self._execute(query, (id,), fetch_one=True)
    
    def get_or_create_client(self, client_name, phone):
        """
        looks for client by phone
        if not found -> creates new one
        returns client_id
        """
       
        query_select = """
            SELECT id
            FROM clients
            WHERE phone = %s
        """

        result = self._execute(query_select, (phone,), fetch_one=True)

        if result:
            return result['id']

        # Создание нового клиента
        query_insert = """
            INSERT INTO clients (client_name, phone)
            VALUES (%s, %s)
            RETURNING id
        """

        result = self._execute(query_insert, (client_name, phone), fetch_one=True, commit=True)

        if result:
            return result['id']
        else:
            raise Exception("failed to create client")

    def create_appointment(self,
                        client_name,
                        phone, 
                        service_id, 
                        appointment_datetime, 
                        client_wish, 
                        master_id=1):
        """
        creates appointment for a service
        """
        # Получаем или создаем клиента
        client_id = self.get_or_create_client(client_name, phone)
        
        # Создаем запись
        query_insert = """
            INSERT INTO appointments 
            (client_id, master_id, service_id, client_wish, date)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """
        result = self._execute(
            query_insert, 
            (client_id, master_id, service_id, client_wish, appointment_datetime),
            fetch_one=True,
            commit=True
        )
        
        if result:
            return result['id']
        else:
            raise Exception("Failed to create appointment")                         

from database.db import connect_db
service_model = AppointmentModel(connect_db)