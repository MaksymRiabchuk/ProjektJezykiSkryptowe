from memory_profiler import profile

from entities.people.Person import Person


class Teacher(Person):
    ## @profile
    def __init__(self, name, lastname, age, salary):
        super().__init__(name, lastname, age)
        self.salary = salary

    # @profile
    def printPersonInfo(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Lastname: ", self.lastname)
        print("Age: ", self.age)
        print("Salary: ", self.salary)

    # @profile
    def addGrade(self, subject, student, grade, updated_at=None):
        student.addGrade(subject, self, grade, updated_at)
