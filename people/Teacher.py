from people.Person import Person


class Teacher(Person):
    def __init__(self, name, lastname, age, salary):
        super().__init__(name, lastname, age)
        self.salary = salary

    def printPersonInfo(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Lastname: ", self.lastname)
        print("Age: ", self.age)
        print("Salary: ", self.salary)

    def addGrade(self, subject, student, grade):
        student.addGrade(subject, self, grade)
