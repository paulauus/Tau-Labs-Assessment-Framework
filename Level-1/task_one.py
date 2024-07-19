"""This is Week 2 Assessment on OOP."""

from datetime import date
from dateutil.relativedelta import relativedelta

class Trainee:
    """This class creates a Trainee based on their name, email and age."""
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> float:
        """Returns the age of the Trainee."""
        today = date.today()
        # relativedelta provides the difference in years
        age = relativedelta(today, self.date_of_birth).years
        return float(age)

class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score
        if self.score < 0 or self.score > 100:
            raise ValueError("Score can be between 0 and 100.")
        valid_types = ["technical", "multiple-choice"]
        if type not in valid_types:
            raise ValueError("Not a valid type.")

if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
