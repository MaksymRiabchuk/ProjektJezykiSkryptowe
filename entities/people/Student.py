import time
from datetime import datetime

from entities.Grade import Grade
from entities.people.Person import Person


class Student(Person):
    def __init__(self, name, lastname, age, yearOfStudy, grades):
        super().__init__(name, lastname, age)
        self.yearOfStudy = yearOfStudy
        self.grades = grades

    def printPersonInfo(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Lastname: ", self.lastname)
        print("Age: ", self.age)
        print("Year of study: ", self.yearOfStudy)

    def addGrade(self, subject, teacher, mark, updated_at=None):
        if updated_at:
            current_unix_time_int = updated_at
        else:
            current_unix_time_int = int(time.time())
        grade = Grade(subject, self, mark, teacher, current_unix_time_int, current_unix_time_int)
        self.grades.append(grade)
        return grade

    def getGradeForToday(self, subject, teacher):
        for grade in self.grades:
            grade_date = datetime.utcfromtimestamp(grade.updated_at)
            now = datetime.utcnow()
            if (grade_date.date() == now.date() and
                    grade.subject == subject and
                    grade.teacher == teacher):
                return grade
        return None

    def updateGradeWithTheSameDate(self, subject, teacher, mark):
        for grade in self.grades:
            grade_date = datetime.utcfromtimestamp(grade.updated_at)
            now = datetime.utcnow()
            if (grade_date.date() == now.date() and
                    grade.subject == subject and
                    grade.teacher == teacher):
                grade.grade = mark
                return True
        return False

    def updateGrade(self, subject, teacher, mark, date):
        for grade in self.grades:
            grade_date = datetime.utcfromtimestamp(grade.updated_at)
            if (grade_date.date().day == date.day and grade_date.date().year == date.year and
                    grade_date.date().month == date.month and
                    grade.subject == subject and
                    grade.teacher == teacher):
                grade.grade = mark
                return True
        return False
