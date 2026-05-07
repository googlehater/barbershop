# import sqlalchemy as sa
# at 2nd lab we should use sql only. no orm



class AppointmentModel:
    def __init__(self, id, client_id, master_id, service_id, client_wish, date, created_at, status):
        self.id = id
        self.client_id = client_id
        self.master_id = master_id
        self.service_id = service_id
        self.client_wish = client_wish
        self.date = date
        self.created_at = created_at

    def get_all():
        pass

    def get_by_id(id):
        pass


