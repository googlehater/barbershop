import psycopg2
from psycopg2.extras import RealDictCursor


class ServiceModel:
    # ToDo: BaseModel for theese 2 funcs
    def __init__(self, get_connection_func):
        """
        get_connection_func - for psycopg2 connection
        """
        self.get_conn = get_connection_func

    def _execute(self, query, params=None, fetch=True, fetch_one=False):
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
        finally:
            conn.close()

    # crud

    def get_all_services(self):
        query = "SELECT * FROM services ORDER BY id"
        return self._execute(query)
    
    def get_by_id(self, id):
        query = "SELECT * FROM services WHERE id = %s"
        return self._execute(query, (id,), fetch_one=True)
    
    def create_service(self, name, duration, price, description=None):
        query = """
        INSERT INTO services (services_name, duration_minutes, price, description)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
        result = self._execute(query, (name, duration, price, description), fetch_one=True)
        return result['id'] if result else None
    
    def update_service(self, service_id, name=None, duration=None, price=None, description=None):
        fields = {}
        if name is not None:
            fields['services_name'] = name
        if duration is not None:
            fields['duration_minutes'] = duration
        if price is not None:
            fields['price'] = price
        if description is not None:
            fields['description'] = description

        if not fields:
            return False
        
        set_clause = ", ".join([f"{k} = %s" for k in fields.keys()])
        values = list(fields.values()) + [service_id]
        query = f"UPDATE services SET {set_clause} WHERE id = %s"
        self._execute(query, values, fetch=False)

        return True
    
    def delete_service(self, service_id):
        query = "DELETE FROM services WHERE id = %s"
        self._execute(query, (service_id,), fetch=False)

from database.db import connect_db
service_model = ServiceModel(connect_db) # тут DI, модель не знает откуда connection!
