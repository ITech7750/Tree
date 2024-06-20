# преподаватели

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __eq__(self, other):
        if isinstance(other, Teacher):
            
            return self.name == other.name and self.subject == other.subject
        return False

    def __lt__(self, other):
        return (self.name, self.subject) < (other.name, other.subject)

    def __str__(self):
        return f"{self.name}, {self.subject}"
