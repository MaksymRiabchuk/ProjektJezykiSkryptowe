import csv
from collections import defaultdict
from functools import wraps, reduce

from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from memory_profiler import profile

from entities.Subject import Subject
from exceptions.ValidationException import ValidationException
from entities.people.Student import Student
from entities.people.Teacher import Teacher
from datetime import datetime


# @profile
def isIntInRange(intVal, maxVal, minVal=1):
    try:
        intTarget = int(intVal)
    except ValueError:
        return False
    else:
        if minVal > intTarget or maxVal < intTarget:
            return False
        else:
            return True


# @profile
def validate_teacher_uniqueness(method):
    @wraps(method)
    def wrapper(self, lastname, name, age, salary, newLastname,
                newName, *args, **kwargs):
        if not isIntInRange(age, 60, 20):
            raise ValidationException("Age of new teacher must be a"
                                      " number in range 20-60")
        elif not isIntInRange(salary, 8000, 2000):
            raise ValidationException("Salary of new teacher"
                                      " must be a number in range 2000-8000")

        if name is not None:
            if self.checkTeacher(newLastname, newName):
                raise ValidationException("Teacher with this"
                                          " lastname and name already exists!")
        else:
            if self.checkTeacherOnlyByLastname(newLastname):
                raise ValidationException("Teacher with this"
                                          " lastname already exists!")

        return method(self, lastname, name,
                      age, salary, newLastname, newName, *args, **kwargs)

    return wrapper


# @profile
def validate_student_uniqueness(method):
    @wraps(method)
    def wrapper(self, lastname, name, age,
                yearOfStudy, newLastname, newName, *args, **kwargs):
        if not isIntInRange(age, 18, 6):
            raise ValidationException("Age of new student must"
                                      " be a number in range 6-18")
        elif not isIntInRange(yearOfStudy, 12, 1):
            raise ValidationException("Year of study of new student must"
                                      " be a number in range 1-12")

        if name is not None:
            if self.checkStudent(newLastname, newName):
                raise ValidationException("Student with this "
                                          "lastname and name already exists!")
        else:
            if self.cehcStudentOnlyByLastname(newLastname):
                raise ValidationException("Student with this "
                                          "lastname already exists!")

        return method(self, lastname, name, age,
                      yearOfStudy, newLastname, newName, *args, **kwargs)

    return wrapper


# @profile
def validate_subject_uniqueness(method):
    @wraps(method)
    def wrapper(self, name, startGrade, endGrade, newName,
                newStartGrade, newEndGrade, *args, **kwargs):
        if not isIntInRange(startGrade, 12, 1):
            raise ValidationException("Start grade of new subject must"
                                      " be a number in range 6-18")
        elif not isIntInRange(endGrade, 12, 1):
            raise ValidationException("End grade of new subject must"
                                      " be a number in range 1-12")

        if name is not None:
            if self.checkSubject(name):
                raise ValidationException("Subject with this"
                                          " name already exists!")

        return method(self, name, newName, newStartGrade,
                      newEndGrade, *args, **kwargs)

    return wrapper


# Comment
class School:
    # @profile
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.people = []
        self.subjects = []

    # @profile
    def getAllStudents(self):
        students = set()
        for i in self.people:
            if isinstance(i, Student):
                students.add(i)
        return students

    # @profile
    def getAllTeachers(self):
        teachers = set()
        for i in self.people:
            if isinstance(i, Teacher):
                teachers.add(i)
        return teachers

    # @profile
    def getAllGrades(self):
        students = self.getAllStudents()
        grades = []
        for student in students:
            for grade in student.grades:
                grades.append(grade)

        return grades

    # @profile
    def getAllGradesBySubjects(self):
        grades = self.getAllGrades()
        dictGrades = reduce(
            lambda acc, grade: acc | {grade.subject: grade.grade}
            if grade.subject not in acc else acc,
            grades,
            {}
        )
        return dictGrades

    # @profile
    def addStudent(self, name, lastname, age, yearOfStudy, grades):
        if not isIntInRange(age, 18, 6):
            raise ValidationException("Age must be "
                                      "a valid integer between 6 and 18")
        elif not isIntInRange(yearOfStudy, 12, 1):
            raise ValidationException("Year of studying must be"
                                      " a valid integer between 1 and 12")
        elif self.checkStudent(lastname, name):
            raise ValidationException("Student with this "
                                      "lastname and name already exists!")
        newStudent = Student(name, lastname, age, yearOfStudy, grades)
        self.people.append(newStudent)
        return newStudent

    # @profile
    @validate_student_uniqueness
    def updateStudent(self, lastname, name, age,
                      yearOfStudy, newLastname, newName):
        if name is not None:
            student = self.getStudentByLastnameName(lastname, name)
        else:
            student = self.getStudentByLastname(lastname)

        if student is None:
            raise ValidationException("Student not found!")
        student.lastname = newLastname
        student.name = newName
        student.age = age
        student.yearOfStudy = yearOfStudy
        print(f"Student {student.lastname} {student.name}"
              f" updated successfully!")
        return student

    # @profile
    def addGrade(self, student, teacher, subject,
                 mark, updated_at=None):
        if not isIntInRange(mark, 5, 1):
            raise ValidationException("Mark must be "
                                      "a valid integer between 1 and 5")
        elif not self.checkTeacher(teacher.lastname, teacher.name):
            raise ValidationException("Teacher not found!")
        elif not self.checkSubject(subject.name):
            raise ValidationException("Subject not found!")
        elif not self.checkStudent(student.lastname, student.name):
            raise ValidationException("Student not found!")

        newGrade = student.addGrade(subject, teacher, mark, updated_at)
        return newGrade

    # @profile
    def addSubject(self, name, startGrade, endGrade):
        if not isIntInRange(startGrade, 12):
            raise ValidationException("Start grade of "
                                      "subject must be a number in range 1-12")
        elif not isIntInRange(endGrade, 12):
            raise ValidationException("End grade of "
                                      "subject must be "
                                      "a number in range 1-12")
        elif self.checkSubject(name):
            raise ValidationException("Subject with "
                                      "this name already exists!")

        newSubject = Subject(name, startGrade, endGrade)
        self.subjects.append(newSubject)
        return newSubject

    # @profile
    @validate_subject_uniqueness
    def updateSubject(self, name, newName, newStartGrade, newEndGrade):
        subject = self.getSubjectByName(name)

        if subject is None:
            raise ValidationException("Subject not found!")
        subject.lastname = newName
        subject.startGrade = newStartGrade
        subject.endGrade = newEndGrade

        print(f"Subject {subject.name} updated successfully!")
        return subject

    # @profile
    def addTeacher(self, lastname, name, age, salary):
        if not isIntInRange(age, 60, 20):
            raise ValidationException("Age of new teacher must be"
                                      " a number in range 20-60")
        elif not isIntInRange(salary, 8000, 2000):
            raise ValidationException("Salary of new teacher must be"
                                      " a number in range 2000-8000")
        elif self.checkTeacher(lastname, name):
            raise ValidationException("Teacher with "
                                      "this lastname and name already exists!")
        newTeacher = Teacher(name, lastname, age, salary)
        self.people.append(newTeacher)
        return newTeacher

    # @profile
    @validate_teacher_uniqueness
    def updateTeacher(self, lastname, name, age,
                      salary, newLastname, newName):
        if name is not None:
            teacher = self.getTeacherByLastnameName(lastname, name)
        else:
            teacher = self.getTeacherByLastname(lastname)

        if teacher is None:
            raise ValidationException("Teacher not found!")
        teacher.lastname = newLastname
        teacher.name = newName
        teacher.age = age
        teacher.salary = salary

        print(f"Teacher {teacher.lastname} {teacher.name}"
              f" updated successfully!")
        return teacher

    # @profile
    def checkSubject(self, nameOfSubject):
        for subject in self.subjects:
            if subject.name.lower() == nameOfSubject.lower():
                return True
        return False

    # @profile
    def checkTeacherOnlyByLastname(self, lastnameOfTeacher):
        k = 0
        for teacher in self.getAllTeachers():
            if teacher.lastname.lower() == lastnameOfTeacher.lower():
                k += 1
        return k

    # @profile
    def checkTeacher(self, lastnameOfTeacher, nameOfTeacher):
        for teacher in self.getAllTeachers():
            if (teacher.lastname.lower() == lastnameOfTeacher.lower()
                    and teacher.name.lower() == nameOfTeacher.lower()):
                return True
        return False

    # @profile
    def checkStudentOnlyByLastname(self, lastnameOfStudent):
        k = 0
        for student in self.getAllStudents():
            if student.lastname.lower() == lastnameOfStudent.lower():
                k += 1
        return k

    # @profile
    def checkStudent(self, lastnameOfStudent, nameOfStudent):
        for student in self.getAllStudents():
            if (student.lastname.lower() == lastnameOfStudent.lower()
                    and student.name.lower() == nameOfStudent.lower()):
                return True
        return False

    # @profile
    def printAllSubjects(self):
        if len(self.subjects) == 0:
            print("---------------------------")
            print("There are no subjects")
            print("---------------------------")
        else:
            print("---------------------------")
            for subject in self.subjects:
                print(f"{subject.name}: "
                      f"{subject.startGrade}-{subject.endGrade}")
            print("---------------------------")

    # @profile
    def printAllTeachers(self):
        if len(self.subjects) == 0:
            print("---------------------------")
            print("There are no subjects")
            print("---------------------------")
        else:
            print("---------------------------")
            teachers_strings = list(
                map(lambda t: f"{t.lastname} {t.name}, {t.age},"
                              f" {t.salary}$", self.getAllTeachers()))
            for line in teachers_strings:
                print(line)

            print("---------------------------")

    # @profile
    def printAllStudentsWithoutGrades(self):
        if len(self.subjects) == 0:
            print("---------------------------")
            print("There are no subjects")
            print("---------------------------")
        else:
            print("---------------------------")
            for student in self.getAllStudents():
                print(f"{student.lastname} {student.name},"
                      f" {student.age} y.o, {student.yearOfStudy}-th grade")
            print("---------------------------")

    # @profile
    def printAllGradesForSubject(self, subjectName, start_month, end_month):
        dates = set()
        for grade in self.getAllGrades():
            if (grade.subject.name.lower() == subjectName.lower()
                    and end_month >= datetime.utcfromtimestamp(
                        grade.updated_at).month and
                    start_month <=
                    datetime.utcfromtimestamp(grade.updated_at).month and
                    datetime.utcfromtimestamp(grade.updated_at).year ==
                    datetime.today().year):
                date_only = datetime.utcfromtimestamp(grade.updated_at).date()
                dates.add(date_only)
        if len(dates) == 0:
            print("---------------------------")
            print("There are no grades for provided month.")
            print("---------------------------")
            return
        dates = sorted(dates)

        maxLen = max(len(student.lastname + " " + student.name)
                     for student in self.getAllStudents())

        print("-" * (len(dates) * 9), end="")
        print("-" * (maxLen + 2))
        print(" " * (maxLen + 2), end="")
        for date in dates:
            print(date.strftime('%d.%m.%y').center(8), end=" ")
        print()

        student_grades_by_date = {}
        for student in self.getAllStudents():
            student_key = student.lastname + " " + student.name
            student_grades_by_date[student_key] = {}
            for grade in student.grades:
                if grade.subject.name.lower() == subjectName.lower():
                    date_only = (datetime.utcfromtimestamp(grade.updated_at)
                                 .date())
                    student_grades_by_date[student_key][date_only] \
                        = grade.grade

        for student_key, grades_by_date in student_grades_by_date.items():
            print(student_key.ljust(maxLen + 2), end="")
            for date in dates:
                grade = str(grades_by_date.get(date, "")).center(8)
                print(grade, end=" ")
            print()

        print("-" * (len(dates) * 9), end="")
        print("-" * (maxLen + 2))

    # @profile
    def printAllGradesForStudent(self, studentLastname,
                                 studentName, start_month, end_month):
        student = self.getStudentByLastnameName(studentLastname, studentName)
        if not student:
            print("No student found with this name.")
            return

        dates = set()
        for grade in student.grades:
            grade_date = datetime.utcfromtimestamp(grade.updated_at)
            if (start_month <= grade_date.month <= end_month and
                    grade_date.year == datetime.today().year):
                dates.add(grade_date.date())

        if len(dates) == 0:
            print("---------------------------")
            print("There are no grades for provided month.")
            print("---------------------------")
            return

        dates = sorted(dates)

        subjects = set(grade.subject.name for grade in student.grades)

        maxLen = max(len(subject) for subject in subjects)

        print("-" * (len(dates) * 9), end="")
        print("-" * (maxLen + 2))
        print(" " * (maxLen + 2), end="")
        for date in dates:
            print(date.strftime('%d.%m.%y').center(8), end=" ")
        print()

        grades_by_subject_and_date = {}
        for subject in subjects:
            grades_by_subject_and_date[subject] = {}
            for grade in student.grades:
                if grade.subject.name == subject:
                    grade_date = (
                        datetime.utcfromtimestamp(grade.updated_at).date())
                    grades_by_subject_and_date[subject][grade_date] \
                        = grade.grade

        for subject, grades_by_date in grades_by_subject_and_date.items():
            print(subject.ljust(maxLen + 2), end="")
            for date in dates:
                grade = str(grades_by_date.get(date, "")).center(8)
                print(grade, end=" ")
            print()

        print("-" * (len(dates) * 9), end="")
        print("-" * (maxLen + 2))

    # @profile
    def getTeacherByLastname(self, lastname):
        if self.checkTeacherOnlyByLastname(lastname):
            for teacher in self.getAllTeachers():
                if teacher.lastname.lower() == lastname.lower():
                    return teacher
        return None

    # @profile
    def getTeacherByLastnameName(self, lastname, name):
        if self.checkTeacher(lastname, name):
            for teacher in self.getAllTeachers():
                if (teacher.lastname.lower() ==
                        lastname.lower() and
                        teacher.name.lower() == name.lower()):
                    return teacher
        return None

    # @profile
    def getStudentByLastname(self, lastname):
        if self.checkStudentOnlyByLastname(lastname):
            for student in self.getAllStudents():
                if student.lastname.lower() == lastname.lower():
                    return student
        return None

    # @profile
    def getStudentByLastnameName(self, lastname, name):
        if self.checkStudent(lastname, name):
            for student in self.getAllStudents():
                if (student.lastname.lower() == lastname.lower()
                        and student.name.lower() == name.lower()):
                    return student
        return None

    # @profile
    def getSubjectByName(self, subjectName):
        if self.checkSubject(subjectName):
            for subject in self.subjects:
                if subject.name.lower() == subjectName.lower():
                    return subject
        return None

    # @profile
    def findSubject(self, string):
        found_subjects = list(filter(
            lambda subject:
            string.lower() in subject.name.lower(), self.subjects))

        if not found_subjects:
            print("---------------------------")
            print("No matching subjects found.")
            print("---------------------------")
        elif len(found_subjects) == 1:
            print("---------------------------")
            print(
                f"Found subject: {found_subjects[0].name} "
                f"(from grade {found_subjects[0].startGrade}"
                f" to {found_subjects[0].endGrade})")
            print("---------------------------")
        else:
            print("---------------------------")
            print("Found multiple subjects:")
            for idx, subject in enumerate(found_subjects, start=1):
                print(f"{idx}. {subject.name} "
                      f"(from grade {subject.startGrade}"
                      f" to {subject.endGrade})")
            print("---------------------------")

    # @profile
    def findTeacher(self, string):
        found_teachers = [teacher for teacher
                          in self.getAllTeachers()
                          if string.lower() in teacher.name.lower()]

        if not found_teachers:
            print("---------------------------")
            print("No matching teachers found.")
            print("---------------------------")
        elif len(found_teachers) == 1:
            print("---------------------------")
            print(
                f"Found teacher: {found_teachers[0].lastname} "
                f"{found_teachers[0].name} {found_teachers[0].age} "
                f"y.o. {found_teachers[0].salary}$")
            print("---------------------------")
        else:
            print("---------------------------")
            print("Found multiple teachers:")
            for idx, teacher in enumerate(found_teachers, start=1):
                print(f"{idx}. {teacher.lastname} {teacher.name}"
                      f" {teacher.age} y.o. {teacher.salary}$")
            print("---------------------------")

    # @profile
    def findStudent(self, string):
        found_students = [teacher for teacher
                          in self.getAllStudents() if string.lower()
                          in teacher.name.lower()]

        if not found_students:
            print("---------------------------")
            print("No matching teachers found.")
            print("---------------------------")
        elif len(found_students) == 1:
            print("---------------------------")
            print(
                f"Found teacher: {found_students[0].lastname}"
                f" {found_students[0].name} {found_students[0].age}"
                f" y.o. {found_students[0].yearOfStudy}th")
            print("---------------------------")
        else:
            print("---------------------------")
            print("Found multiple teachers:")
            for idx, student in enumerate(found_students, start=1):
                print(f"{idx}. {student.lastname} "
                      f"{student.name} {student.age} "
                      f"y.o. {student.yearOfStudy}th")
            print("---------------------------")

    # @profile
    def exportStudentsToCSV(self, filename="students.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(("Lastname", "Name", "Age", "YearOfStudy"))
            for student in self.getAllStudents():
                writer.writerow([student.lastname,
                                 student.name, student.age,
                                 student.yearOfStudy])

    # @profile
    def exportTeachersToCSV(self, filename="teachers.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(("Lastname", "Name", "Age", "Salary"))
            for teacher in self.getAllTeachers():
                writer.writerow([teacher.lastname,
                                 teacher.name, teacher.age, teacher.salary])

    # @profile
    def exportSubjectsToCSV(self, filename="subjects.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(("Name", "StartGrade", "EndGrade"))
            for subject in self.subjects:
                writer.writerow([subject.name,
                                 subject.startGrade, subject.endGrade])

    # @profile
    def exportGradesToCSV(self, filename="grades.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ("Student Lastname", "Student Name", "Subject",
                 "Teacher Lastname", "Teacher Name", "Grade", "Date"))
            for grade in self.getAllGrades():
                student = grade.student
                writer.writerow([
                    student.lastname,
                    student.name,
                    grade.subject.name,
                    grade.teacher.lastname,
                    grade.teacher.name,
                    grade.grade,
                    datetime.utcfromtimestamp(grade.updated_at)
                    .strftime('%d.%m.%Y %H:%M:%S')
                ])

    # @profile
    def importStudentsFromCSV(self, filename="students.csv"):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row["Name"],
                        row["Lastname"],
                        int(row["Age"]),
                        int(row["YearOfStudy"]),
                        []
                    )
                    self.people.append(student)
        except FileNotFoundError:
            raise ValidationException(f"File {filename} does not exits")

    # @profile
    def importTeachersFromCSV(self, filename="teachers.csv"):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    teacher = Teacher(
                        row["Name"],
                        row["Lastname"],
                        int(row["Age"]),
                        int(row["Salary"])
                    )
                    self.people.append(teacher)
        except FileNotFoundError:
            raise ValidationException(f"File {filename} does not exits")

    # @profile
    def importSubjectsFromCSV(self, filename="subjects.csv"):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    subject = Subject(
                        row["Name"],
                        int(row["StartGrade"]),
                        int(row["EndGrade"])
                    )
                    self.subjects.append(subject)
        except FileNotFoundError:
            raise ValidationException(f"File {filename} does not exits")

    # @profile
    def importGradesFromCSV(self, filename="grades.csv"):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = self.getStudentByLastnameName(
                        row["Student Lastname"], row["Student Name"])
                    teacher = self.getTeacherByLastnameName(
                        row["Teacher Lastname"], row["Teacher Name"])
                    subject = self.getSubjectByName(row["Subject"])
                    if student and teacher and subject:
                        mark = int(row["Grade"])
                        date_obj = datetime.strptime(row["Date"],
                                                     '%d.%m.%Y %H:%M:%S')
                        student.addGrade(subject, teacher, mark,
                                         date_obj.timestamp())
        except FileNotFoundError:
            raise ValidationException(f"File {filename} does not exits")

    # @profile
    def plot_grades_per_subject(self):
        grades = self.getAllGrades()
        if not grades:
            print("---------------------------")
            print("No grades to show.")
            print("---------------------------")
            return

        subject_grades = defaultdict(list)

        for grade in grades:
            date = datetime.utcfromtimestamp(grade.updated_at)
            subject_grades[grade.subject.name].append((date, grade.grade))

        plt.figure(figsize=(12, 6))

        for subject, data in subject_grades.items():
            data.sort(key=lambda x: x[0])
            dates, marks = zip(*data)
            plt.plot(dates, marks, marker='o', label=subject)

        plt.xlabel("Date")
        plt.ylabel("Grade")
        plt.title("Grades")
        plt.legend()
        plt.grid(True)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
        plt.gcf().autofmt_xdate()

        plt.ylim(0.5, 5.5)
        plt.yticks([1, 2, 3, 4, 5])

        plt.savefig('grades.png')
        plt.show()
