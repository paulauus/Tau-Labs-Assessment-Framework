# pylint: disable=too-few-public-methods
"""Level 2 of Week 2 Assessment."""

from datetime import date
from dateutil.relativedelta import relativedelta
#####
#
# COPY YOUR CODE FROM LEVEL 2 BELOW
#
#####

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
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz
        pass

    def mark(self) -> float:
        total_score = 0
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                total_score += 1
        max_score = len(self._quiz.questions)
        final_mark = float(total_score * 100 / max_score)
        return final_mark



if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
