import datetime

from memory_profiler import profile

from entities.School import isIntInRange
from exceptions.ValidationException import ValidationException


# @profile
def getInputDataForFindSubject(school):
    providedStr = input("Provide name of the subject: ")
    school.findSubject(providedStr)


# @profile
def getInputDataForFindTeacher(school):
    providedStr = input("Provide lastname of the teacher: ")
    school.findTeacher(providedStr)


# @profile
def getInputDataForFindStudent(school):
    providedStr = input("Provide lastname of the student: ")
    school.findStudent(providedStr)


# @profile
def getInputDataForUpdateGrade(school):
    while True:
        subjectName = input("Name of the subject "
                            "(show - to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no subject with this name!")
        else:
            break

    while True:
        teacherLastname = input("Lastname of the teacher"
                                " (show - to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            break
        else:
            while True:
                teacherName = input("Name of the teacher "
                                    "(show - to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher"
                                              " with this name and lastname!")
                else:
                    teacher = (school.
                               getTeacherByLastnameName(teacherLastname,
                                                        teacherName))
                    break
            break

    while True:
        studentLastname = input("Lastname of the student"
                                " (show - to print list of all students): ")
        if studentLastname == "show":
            school.printAllStudentsWithoutGrades()
        elif school.checkStudentOnlyByLastname(studentLastname) == 1:
            student = school.getStudentByLastname(studentLastname)
            break
        else:
            while True:
                studentName = input("Name of the student "
                                    "(show - to print list of all students): ")
                if studentName == "show":
                    school.printAllStudentsWithoutGrades()
                elif not school.checkStudent(studentLastname, studentName):
                    raise ValidationException("There is "
                                              "no student with this "
                                              "name and lastname!")
                else:
                    student = school.getStudentByLastnameName(
                        studentLastname, studentName)
                    break
            break
    while True:
        date = input("Provide the date of mark (dd.mm.yyyy): ")
        try:
            parsed_date = datetime.datetime.strptime(date, "%d.%m.%Y")
            date = parsed_date
            break
        except ValueError:
            print("Invalid format date try again!")

    subject = school.getSubjectByName(subjectName)
    newMark = int(input("New mark: "))
    if not isIntInRange(newMark, 5):
        raise ValidationException("Mark must be between 1 and 5!")

    newGrade = student.updateGrade(subject, teacher,
                                   newMark, date)
    if not newGrade:
        raise ValidationException("There is"
                                  " no grade with provided parameters!")
    else:
        print("---------------------------")
        print("Grade updated successfully!")
        print("---------------------------")


# @profile
def inputGradeForStudent(student, school):
    while True:
        subjectName = input("Name of the subject "
                            "(show - to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no subject with this name!")
        else:
            break

    while True:
        teacherLastname = input("Lastname of the teacher "
                                "(show - to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            break
        else:
            while True:
                teacherName = input("Name of the teacher (show"
                                    " - to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher"
                                              " with this name and lastname!")
                else:
                    teacher = school.getTeacherByLastnameName(
                        teacherLastname, teacherName)
                    break
            break

    subject = school.getSubjectByName(subjectName)

    mark = int(input("Mark: "))
    if not isIntInRange(mark, 5):
        raise ValidationException("Mark must be between 1 and 5!")

    existing_grade = student.getGradeForToday(subject, teacher)
    if existing_grade is not None:
        student.updateGradeWithTheSameDate(subject, teacher, mark)
        print("Grade updated successfully!")
    else:
        student.addGrade(subject, teacher, mark)
        print("---------------------------")
        print("Grade added successfully!")
        print("---------------------------")

    choice = input("Continue? ")
    if choice.lower() in ["yes", "y"] or isIntInRange(choice, 1) == 1:
        inputGradeForStudent(student, school)


# @profile
def getInputDataForAddSubject(school):
    subjectName = input("Provide name of the subject: ")
    startGrade = int(input("Provide grade from"
                           " which this subject should be taught: "))
    endGrade = int(input("Provide grade till"
                         " which this subject should be taught: "))
    newSubject = school.addSubject(subjectName, startGrade, endGrade)
    if newSubject is None:
        raise ValidationException("Exception happened"
                                  " while validating"
                                  " the data for the subject!")
    print("---------------------------")
    print("Subject added successfully!")
    print("---------------------------")


# @profile
def getInputDataForAddTeacher(school):
    teacherName = input("Provide name of new teacher: ")
    teacherLastname = input("Provide lastname of new teacher: ")
    teacherAge = int(input("Provide age of new teacher: "))
    teacherSalary = float(input("Provide salary of new teacher "))
    newSubject = school.addTeacher(teacherLastname,
                                   teacherName, teacherAge, teacherSalary)
    if newSubject is None:
        raise ValidationException("Exception happened "
                                  "while validating the data for the teacher!")
    print("---------------------------")
    print("Teacher added successfully!")
    print("---------------------------")


# @profile
def getInputDataForUpdateTeacher(school):
    while True:
        teacherLastname = input("Lastname of the teacher (show - "
                                "to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            if not (teacher is None):
                newTeacherLastname = input("New lastname of the teacher: ")
                newTeacherName = input("New name of the teacher: ")
                newTeacherAge = input("New name of the teacher: ")
                newTeacherSalary = input("New name of the teacher: ")
                school.updateTeacher(teacher.lastname, teacher.name,
                                     newTeacherAge, newTeacherSalary,
                                     newTeacherLastname, newTeacherName)
            break
        else:
            while True:
                teacherName = input("Name of the teacher (show -"
                                    " to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher"
                                              " with this name and lastname!")
                else:
                    teacher = school.getTeacherByLastnameName(
                        teacherLastname, teacherName)
                    if not (teacher is None):
                        newTeacherLastname = input("New lastname of "
                                                   "the teacher: ")
                        newTeacherName = input("New name of the teacher: ")
                        newTeacherAge = int(input("New age of the teacher: "))
                        newTeacherSalary = float(input("New salary of"
                                                       " the teacher: "))
                        school.updateTeacher(teacher.lastname,
                                             teacher.name, newTeacherAge,
                                             newTeacherSalary,
                                             newTeacherLastname,
                                             newTeacherName)
                    break
            break


# @profile
def getInputDataForUpdateSubject(school):
    while True:
        subjectName = input("Name of the subject (show -"
                            " to print list of all subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        else:
            if not school.checkSubject(subjectName):
                raise ValidationException("There is no subject"
                                          " with this name!")
            else:
                subject = school.getSubjectByName(subjectName)
                if not (subject is None):
                    newSubjectName = input("New name of the subject: ")
                    newSubjectStartGrade = input("New start grade"
                                                 " of the subject: ")
                    newSubjectEndGrade = int(input("New end grade"
                                                   " of the subject: "))
                    school.updateTeacher(subject.name, subject.startGrade,
                                         subject.endGrade, newSubjectName,
                                         newSubjectStartGrade,
                                         newSubjectEndGrade)
        break


# @profile
def getInputDataForUpdateStudent(school):
    while True:
        studentLastname = input("Lastname of the student (show - "
                                "to print list of all students): ")
        if studentLastname == "show":
            school.printAllStudentsWithoutGrades()
        elif school.checkStudentOnlyByLastname(studentLastname) == 1:
            student = school.getStudentByLastname(studentLastname)
            if not (student is None):
                newStudentLastname = input("New lastname of the student: ")
                newStudentName = input("New name of the student: ")
                newStudentAge = input("New age of the student: ")
                newStudentStudyOfYear = input("New year of study"
                                              " of the student: ")
                school.updateStudent(student.lastname,
                                     student.name, newStudentAge,
                                     newStudentStudyOfYear,
                                     newStudentLastname,
                                     newStudentName)
            break
        else:
            while True:
                studentName = input("Name of the student (show - "
                                    "to print list of all students): ")
                if studentName == "show":
                    school.printAllStudentsWithoutGrades()
                elif not school.checkStudent(studentLastname, studentName):
                    raise ValidationException("There is no teacher"
                                              " with this name and lastname!")
                else:
                    student = school.getTeacherByLastnameName(
                        studentLastname, studentName)
                    if not (student is None):
                        newStudentLastname = input("New lastname of"
                                                   " the student: ")
                        newStudentName = input("New name of the student: ")
                        newStudentAge = int(input("New age of"
                                                  " the student: "))
                        newStudentYearOfStudy = int(input("New year of"
                                                          " study of "
                                                          "the student: "))
                        school.updateStudent(student.lastname, student.name,
                                             newStudentAge,
                                             newStudentYearOfStudy,
                                             newStudentLastname,
                                             newStudentName)
                    break
            break


# @profile
def getInputDataForAddStudent(school):
    studentName = input("Provide name of new student: ")
    studentLastname = input("Provide lastname of new student: ")
    studentAge = input("Provide age of new student: ")
    studentYearOfStudy = input("Provide year of studying of new student: ")
    newStudent = school.addStudent(studentName, studentLastname,
                                   studentAge, studentYearOfStudy, [])
    if newStudent is None:
        raise ValidationException("Exception happened while "
                                  "validating the data for the student!")

    choice = input("Do you want to provide grades for him?")
    if (isIntInRange(choice, 1) == 1 or choice.lower()
            == "yes" or choice.lower() == "y"):
        inputGradeForStudent(newStudent, school)
    print("---------------------------")
    print("Student added successfully!")
    print("---------------------------")


# @profile
def getInputDataForAddGrade(school):
    while True:
        subjectName = input("Name of the subject (show -"
                            " to print available subjects): ")
        if subjectName == "show":
            school.printAllSubjects()
        elif not school.checkSubject(subjectName):
            raise ValidationException("There is no"
                                      " subject with this name!")
        else:
            break

    while True:
        teacherLastname = input("Lastname of the teacher (show -"
                                " to print list of all teachers): ")
        if teacherLastname == "show":
            school.printAllTeachers()
        elif school.checkTeacherOnlyByLastname(teacherLastname) == 1:
            teacher = school.getTeacherByLastname(teacherLastname)
            break
        else:
            while True:
                teacherName = input("Name of the teacher (show -"
                                    " to print list of all teachers): ")
                if teacherName == "show":
                    school.printAllTeachers()
                elif not school.checkTeacher(teacherLastname, teacherName):
                    raise ValidationException("There is no teacher "
                                              "with this name and lastname!")
                else:
                    teacher = school.getTeacherByLastnameName(
                        teacherLastname, teacherName)
                    break
            break

    while True:
        studentLastname = input("Lastname of the student (show -"
                                " to print list of all students): ")
        if studentLastname == "show":
            school.printAllStudentsWithoutGrades()
        elif school.checkStudentOnlyByLastname(studentLastname) == 1:
            student = school.getStudentByLastname(studentLastname)
            break
        else:
            while True:
                studentName = input("Name of the student (show -"
                                    " to print list of all students): ")
                if studentName == "show":
                    school.printAllStudentsWithoutGrades()
                elif not school.checkStudent(studentLastname, studentName):
                    raise ValidationException("There is no student"
                                              " with this name and lastname!")
                else:
                    student = school.getStudentByLastnameName(
                        studentLastname, studentName)
                    break
            break
    subject = school.getSubjectByName(subjectName)
    mark = int(input("Mark: "))
    if not isIntInRange(mark, 5):
        raise ValidationException("Mark must be between 1 and 5!")

    existing_grade = student.getGradeForToday(subject, teacher)
    if existing_grade is not None:
        newGrade = student.updateGradeWithTheSameDate(subject, teacher, mark)
        if newGrade is None:
            raise ValidationException("Exception happened while"
                                      " validating the data for new grade!")
        else:
            print("---------------------------")
            print("Grade updated successfully!")
            print("---------------------------")
    else:
        newGrade = student.addGrade(subject, teacher, mark,
                                    datetime.datetime.today().timestamp())
        if newGrade is None:
            raise ValidationException("Exception happened while"
                                      " validating the data for new grade!")
        else:
            print("---------------------------")
            print("Grade added successfully!")
            print("---------------------------")
