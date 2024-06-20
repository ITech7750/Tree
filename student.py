# студенты


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.grade == other.grade
        return False

    def __lt__(self, other):
        return (self.name, self.grade) < (other.name, other.grade)

    def __str__(self):
        return f"{self.name}, {self.grade}"
