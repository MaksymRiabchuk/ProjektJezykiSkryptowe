import time

from Grade import Grade
from people.Person import Person


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

    def addGrade(self, subject, teacher, grade):
        current_unix_time_int = int(time.time())
        grade = Grade(subject, self, grade, teacher, current_unix_time_int, current_unix_time_int)
        self.grades.append(grade)
