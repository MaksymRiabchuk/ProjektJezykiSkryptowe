from entities.School import School
from inputFuncs.functions import *

global school
school = School("School", "address")


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
    student = school.addStudent("Stu", "Stul", 12, 11, [])
    student2 = school.addStudent("123", "1234", 12, 10, [])
    teacher = school.addTeacher("Teal", "tea", 21, 2000)
    teacher2 = school.addTeacher("Teal", "tea2", 21, 2000)
    subject = school.addSubject("Math", 1, 12)
    school.addGrade(student, teacher, subject, 5, updated_at=1748937600)
    school.addGrade(student, teacher, subject, 4, updated_at=1749024000)
    school.addGrade(student2, teacher, subject, 3, updated_at=1748851200)
    school.addGrade(student2, teacher, subject, 2, updated_at=1749024000)
    school.addGrade(student2, teacher, subject, 2, updated_at=1751529600)
    school.addGrade(student2, teacher, subject, 2, updated_at=1719993600)
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
                    elif int(secondChoice) == 1:
                        getInputDataForAddSubject(school)
                        break
                    elif int(secondChoice) == 2:
                        getInputDataForUpdateSubject(school)
                        break
                    elif int(secondChoice) == 3:
                        getInputDataForFindSubject(school)
                        break
                    elif int(secondChoice) == 4:
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
                        getInputDataForAddTeacher(school)
                        break
                    elif int(secondChoice) == 2:
                        getInputDataForUpdateTeacher(school)
                        break
                    elif int(secondChoice) == 3:
                        getInputDataForFindTeacher(school)
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
                        getInputDataForAddStudent(school)
                        break
                    elif int(secondChoice) == 2:
                        getInputDataForUpdateStudent(school)
                        break
                    elif int(secondChoice) == 3:
                        getInputDataForFindStudent(school)
                        break
                    elif int(secondChoice) == 4:
                        school.printAllStudentsWithoutGrades()
                        break
                    else:
                        print("Wrong argument, try again!")
            elif int(choice) == 4:
                while True:
                    print("1. Add grade.")
                    print("2. Edit grade.")
                    print("3. Print all grades for the subject.")
                    print("4. Print all grades for the student.")
                    secondChoice = int(input())
                    if secondChoice == "":
                        break
                    elif int(secondChoice) == 1:
                        getInputDataForAddGrade(school)
                        break
                    elif int(secondChoice) == 2:
                        getInputDataForUpdateGrade(school)
                        break
                    elif int(secondChoice) == 3:
                        printAllGradesForSubject()
                        break
                    elif int(secondChoice) == 4:
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
