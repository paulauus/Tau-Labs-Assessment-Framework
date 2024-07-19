# pylint: disable=too-few-public-methods
"""Level 2 of Week 2 Assessment."""

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

    def add_assessment(self, a) -> None:
        """Adds an Assessment object to the list of Trainee's assessments."""
        if not isinstance(a, Assessment):
            raise TypeError("Not a valid")
        return self.assessments.append(a)

    def get_assessment(self, assessment_name: str) -> None:
        """Returns the Assessment object if its name matches method parameter."""
        for item in self.assessments:
            if item.name == assessment_name:
                return item
        return None
            
    def get_assessment_of_type(self, type: str) -> list:
        """Returns the number of instances a type of assessment is present."""
        same_type_assessments = []
        for item in self.assessments:
            if item.type == type:
                same_type_assessments.append(item)
        return same_type_assessments


class Assessment:
    """Create an object for a type of assessment with a title and score."""

    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.type = type
        self.score = score
        if self.score < 0 or self.score > 100:
            raise ValueError("Score can be between 0 and 100.")
        valid_types = ["technical", "multiple-choice", "presentation"]
        if type not in valid_types:
            raise ValueError("Not a valid type.")


class MultipleChoiceAssessment(Assessment):
    """Subclass for a multiple choice assessment type."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "multiple-choice", score)

    def calculate_score(self):
        """Returns a score worth 70% of the assessment."""
        score = self.score * 0.7
        return score


class TechnicalAssessment(Assessment):
    """Subclass for a technical assessment type."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "technical", score)


    def calculate_score(self):
        """Returns a score worth 100% of the assessment."""
        return self.score


class PresentationAssessment(Assessment):
    """Subclass for a presentation assessment type."""

    def __init__(self, name: str, score: float):
        super().__init__(name, "presentation", score)

    def calculate_score(self):
        """Returns a score worth 60% of the assessment."""
        score = self.score * 0.6
        return score

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####

if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
