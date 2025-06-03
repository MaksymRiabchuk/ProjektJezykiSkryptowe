from Subject import Subject
from people.Student import Student
from people.Teacher import Teacher


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.people = []
        self.subjects = []

    def getAllStudents(self):
        students = set()
        for i in self.people:
            if isinstance(i, Student):
                students.add(i)
        return students

    def getAllTeachers(self):
        teachers = set()
        for i in self.people:
            if isinstance(i, Teacher):
                teachers.add(i)
        return teachers

    def getAllGrades(self):
        students = self.getAllStudents()
        grades = []
        for student in students:
            for grade in student.grades:
                grades.append(grade)

        return grades

    def getAllGradesBySubjects(self):
        grades = self.getAllGrades()
        dictGrades = {}
        usedSubjects = []
        for i in range(len(grades)):
            if grades[i].subject.name not in usedSubjects:
                usedSubjects.append(grades[i].subject.name)
                for j in range(len(grades)):
                    if grades[i].subject.name == grades[j].subject.name:
                        dictGrades[grades[i].subject] = grades[j].grade

        return dictGrades

    def addStudent(self, name, lastname, age, yearOfStudy, grades):

        if not (age is int) or not (18 > age >= 6):
            print("Age must be a valid integer between 6 and 17")

        if not (yearOfStudy is int) or not (11 >= yearOfStudy >= 1):
            print("Age must be a valid integer between 1 and 11")

        newStudent = Student(name, lastname, age, yearOfStudy, grades)
        self.people.append(newStudent)

    def addSubject(self, name, startGrade, endGrade):
        if not (startGrade is int):
            print("Start grade of subject must be a number in range 1-11")
        elif not (endGrade is int):
            print("End grade of subject must be a number in range 1-11")

        newSubject = Subject(name, startGrade, endGrade)
        self.subjects.append(newSubject)


