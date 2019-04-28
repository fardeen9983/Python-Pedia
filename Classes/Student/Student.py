# A demo class representing a student entity with a number of details
class Student:

    def __init__(self, name, major, gpa, probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.probation = probation

    def performance(self):
        if self.gpa >= 3.0:
            return "Performing good"
        else:
            return "Need improvement"
