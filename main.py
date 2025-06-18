import datetime

from School import School, isIntInRange
from exceptions.ValidationException import ValidationException


def inputGradeForStudent(student):
    while True:
        subjectName = input("Name of the subject (show - to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no subject with this name!")
        else:
            break

    while True:
        teacherLastname = input("Lastname of the teacher (show - to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            break
        else:
            while True:
                teacherName = input("Name of the teacher (show - to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher with this name and lastname!")
                else:
                    teacher = school.getTeacherByLastnameName(teacherLastname, teacherName)
                    break
            break

    subject = school.getSubjectByName(subjectName)

    mark = int(input("Mark: "))
    if not isIntInRange(mark, 5):
        raise ValidationException("Mark must be between 1 and 5!")

    existing_grade = student.getGradeForToday(subject, teacher)
    if existing_grade is not None:
        student.updateGrade(subject, teacher, mark)
        print("Grade updated successfully!")
    else:
        student.addGrade(subject, teacher, mark)
        print("Grade added successfully!")

    choice = input("Continue? ")
    if choice.lower() in ["yes", "y"] or isIntInRange(choice, 1) == 1:
        inputGradeForStudent(student)


def getInputDataForAddSubject():
    subjectName = input("Provide name of the subject: ")
    startGrade = int(input("Provide grade from which this subject should be taught: "))
    endGrade = int(input("Provide grade till which this subject should be taught: "))
    newSubject = school.addSubject(subjectName, startGrade, endGrade)
    if newSubject is None:
        raise ValidationException("Exception happened while validating the data for the subject!")
    print("Subject added successfully!")


def getInputDataForAddTeacher():
    teacherName = input("Provide name of new teacher: ")
    teacherLastname = input("Provide lastname of new teacher: ")
    teacherAge = int(input("Provide age of new teacher: "))
    teacherSalary = float(input("Provide salary of new teacher "))
    newSubject = school.addTeacher(teacherLastname, teacherName, teacherAge, teacherSalary)
    if newSubject is None:
        raise ValidationException("Exception happened while validating the data for the teacher!")
    print("Teacher added successfully!")


def getInputDataForAddStudent():
    studentName = input("Provide name of new student: ")
    studentLastname = input("Provide lastname of new student: ")
    studentAge = input("Provide age of new student: ")
    studentYearOfStudy = input("Provide year of studying of new student: ")
    newStudent = school.addStudent(studentName, studentLastname, studentAge, studentYearOfStudy, [])
    if newStudent is None:
        raise ValidationException("Exception happened while validating the data for the student!")

    choice = input("Do you want to provide grades for him?")
    if isIntInRange(choice, 1) == 1 or choice.lower() == "yes" or choice.lower() == "y":
        inputGradeForStudent(newStudent)
    print("Student added successfully!")


def getInputDataForAddGrade():
    while True:
        subjectName = input("Name of the subject (show - to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no subject with this name!")
        else:
            break

    while True:
        teacherLastname = input("Lastname of the teacher (show - to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            break
        else:
            while True:
                teacherName = input("Name of the teacher (show - to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher with this name and lastname!")
                else:
                    teacher = school.getTeacherByLastnameName(teacherLastname, teacherName)
                    break
            break

    while True:
        studentLastname = input("Lastname of the student (show - to print list of all students): ")
        if studentLastname == "show":
            school.printAllStudentsWithoutGrades()
        elif school.checkStudentOnlyByLastname(studentLastname) == 1:
            student = school.getStudentByLastname(studentLastname)
            break
        else:
            while True:
                studentName = input("Name of the student (show - to print list of all students): ")
                if studentName == "show":
                    school.printAllStudentsWithoutGrades()
                elif not school.checkStudent(studentLastname, studentName):
                    raise ValidationException("There is no student with this name and lastname!")
                else:
                    student = school.getStudentByLastnameName(studentLastname, studentName)
                    break
            break
    subject = school.getSubjectByName(subjectName)
    mark = int(input("Mark: "))
    if not isIntInRange(mark, 5):
        raise ValidationException("Mark must be between 1 and 5!")

    existing_grade = student.getGradeForToday(subject, teacher)
    if existing_grade is not None:
        newGrade = student.updateGrade(subject, teacher, mark)
        if newGrade is None:
            raise ValidationException("Exception happened while validating the data for new grade!")
        else:
            print("Grade updated successfully!")
    else:
        newGrade = student.addGrade(subject, teacher, mark)
        if newGrade is None:
            raise ValidationException("Exception happened while validating the data for new grade!")
        else:
            print("Grade added successfully!")


def printAllGradesForSubject():
    while True:
        subjectName = input("Name of the subject (show - to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no subject with this name!")
        else:
            break
    start_month = input("Provide starting month: ")
    if start_month == "":
        start_month = datetime.datetime.today().month
        school.printAllGradesForSubject(subjectName, int(start_month), int(start_month))
    elif not isIntInRange(start_month, 12, 1):
        raise ValidationException("Wrong month was provided!")
    else:
        end_month = input("Provide last month: ")
        if end_month == "":
            end_month = datetime.datetime.today().month
            if end_month > int(start_month):
                school.printAllGradesForSubject(subjectName, int(start_month), int(end_month))
            else:
                raise ValidationException("Last month must be after the starting month!")
        elif not isIntInRange(end_month, 12, 1):
            raise ValidationException("Wrong month was provided!")
        elif not isIntInRange(end_month, 12, int(start_month)):
            raise ValidationException("Last month must be after the starting month!")
        else:
            school.printAllGradesForSubject(subjectName, int(start_month), int(end_month))


def printAllGradesForStudent():
    while True:
        studentLastname = input("Lastname of the student (show - to print list of all students): ")
        if studentLastname == "show":
            school.printAllStudentsWithoutGrades()
        elif school.checkStudentOnlyByLastname(studentLastname) == 1:
            student = school.getStudentByLastname(studentLastname)
            break
        else:
            while True:
                studentName = input("Name of the student (show - to print list of all students): ")
                if studentName == "show":
                    school.printAllStudentsWithoutGrades()
                elif not school.checkStudent(studentLastname, studentName):
                    raise ValidationException("There is no student with this name and lastname!")
                else:
                    student = school.getStudentByLastnameName(studentLastname, studentName)
                    break
            break
    start_month = input("Provide starting month: ")
    if start_month == "":
        start_month = datetime.datetime.today().month
        school.printAllGradesForStudent(student.lastname, student.name, int(start_month), int(start_month))
    elif not isIntInRange(start_month, 12, 1):
        raise ValidationException("Wrong month was provided!")
    else:
        end_month = input("Provide last month: ")
        if end_month == "":
            end_month = datetime.datetime.today().month
            if end_month > int(start_month):
                school.printAllGradesForStudent(student.lastname, student.name, int(start_month), int(end_month))
            else:
                raise ValidationException("Last month must be after the starting month!")
        elif not isIntInRange(end_month, 12, 1):
            raise ValidationException("Wrong month was provided!")
        elif not isIntInRange(end_month, 12, int(start_month)):
            raise ValidationException("Last month must be after the starting month!")
        else:
            school.printAllGradesForStudent(student.lastname, student.name, int(start_month), int(end_month))


def printListOfMainMenuChoices():
    print("1. Actions with subjects.")
    print("2. Actions with teachers.")
    print("3. Actions with students.")
    print("4. Actions with grades.")
    print("5. Exit")
    print("Choose action:", end=" ")


def main():
    print("---------------------------")
    global school
    school = School("First school", "address")
    student = school.addStudent("Stu", "Stul", 12, 11, [])
    student2 = school.addStudent("123", "1234", 12, 10, [])
    # student3 = school.addStudent("Stu", "Stul", 12, 10, [])
    teacher = school.addTeacher("Teal", "tea", 21, 2000)
    teacher2 = school.addTeacher("Teal", "tea2", 21, 2000)
    subject = school.addSubject("Math", 1, 12)
    school.addGrade(student, teacher, subject, 5, updated_at=1748937600)
    school.addGrade(student, teacher, subject, 4, updated_at=1749024000)
    school.addGrade(student2, teacher, subject, 3, updated_at=1748851200)
    school.addGrade(student2, teacher, subject, 2, updated_at=1749024000)
    school.addGrade(student2, teacher, subject, 2, updated_at=1751529600)
    school.addGrade(student2, teacher, subject, 2, updated_at=1719993600)
    # school.addGrade(student3, teacher2, subject, 2, updated_at=1751529600)
    # school.addGrade(student3, teacher2, subject, 2, updated_at=1719993600)
    while True:
        try:
            printListOfMainMenuChoices()
            choice = input()
            if choice == "":
                print("Bye!")
                break
            elif int(choice) == 1:
                while True:
                    print("1. Add subject.")
                    print("2. Edit subject.")
                    print("3. Find subject.")
                    print("4. Print all subjects.")
                    print("Choose action:", end=" ")
                    secondChoice = input()
                    if secondChoice == "":
                        break
                    elif secondChoice == 1:
                        getInputDataForAddSubject()
                        break
                    elif secondChoice == 2:
                        break
                    elif secondChoice == 3:
                        break
                    elif secondChoice == 4:
                        school.printAllSubjects()
                        break
            elif int(choice) == 2:
                while True:
                    print("1. Add teacher.")
                    print("2. Edit teacher.")
                    print("3. Find teacher.")
                    print("4. Print all teachers.")
                    print("Choose action:", end=" ")
                    secondChoice = input()
                    if secondChoice == "":
                        break
                    elif int(secondChoice) == 1:
                        getInputDataForAddTeacher()
                        break
                    elif int(secondChoice) == 2:
                        break
                    elif int(secondChoice) == 3:
                        break
                    elif int(secondChoice) == 4:
                        school.printAllTeachers()
                        break
                    else:
                        print("Wrong argument, try again!")
            elif int(choice) == 3:
                while True:
                    print("1. Add student.")
                    print("2. Edit student.")
                    print("3. Find student.")
                    print("4. Print all students.")
                    secondChoice = input()
                    if secondChoice == "":
                        break
                    elif int(secondChoice) == 1:
                        getInputDataForAddStudent()
                        break
                    elif int(secondChoice) == 2:
                        break
                    elif int(secondChoice) == 3:
                        break
                    elif int(secondChoice) == 4:
                        school.printAllStudentsWithoutGrades()
                        break
                    else:
                        print("Wrong argument, try again!")
            elif int(choice) == 4:
                while True:
                    print("1. Add student.")
                    print("2. Edit grade.")
                    print("3. Find grade.")
                    print("4. Print all grades for the subject.")
                    print("5. Print all grades for the student.")
                    secondChoice = int(input())
                    if secondChoice == "":
                        break
                    elif int(secondChoice) == 1:
                        getInputDataForAddGrade()
                        break
                    elif int(secondChoice) == 2:
                        break
                    elif int(secondChoice) == 3:
                        break
                    elif int(secondChoice) == 4:
                        printAllGradesForSubject()
                        break
                    elif int(secondChoice) == 5:
                        printAllGradesForStudent()
                        break
                    else:
                        print("Wrong argument, try again!")
            elif int(choice) == 5:
                print("Bye!")
                break
            else:
                print("Wrong argument, try again!")

        except ValidationException as e:
            print("---------------------------")
            print(e)
            print("---------------------------")


if __name__ == "__main__":
    main()
