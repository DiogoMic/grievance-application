class Admin:
    def __init__(self, database):
        self.database = database

    def view_all_grievances(self):
        return self.database.get_all_grievances()

    def view_grievance_details(self, grievance_id):
        return self.database.get_grievance_by_id(grievance_id)

    def track_requests(self):
        grievances = self.view_all_grievances()
        return {grievance['id']: grievance['status'] for grievance in grievances}

    def update_grievance_status(self, grievance_id, new_status):
        self.database.update_grievance_status(grievance_id, new_status)