class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.grievances = []

    def submit_grievance(self, title, description, category):
        grievance = {
            'title': title,
            'description': description,
            'category': category,
            'status': 'Submitted'
        }
        self.grievances.append(grievance)
        return grievance

    def track_grievances(self):
        return self.grievances

    def validate_form(self, title, description, category):
        if not self.name or not self.email:
            return False, "Name and email are required."
        if not title or not description or not category:
            return False, "Title, description, and category are required."
        return True, "Validation successful."