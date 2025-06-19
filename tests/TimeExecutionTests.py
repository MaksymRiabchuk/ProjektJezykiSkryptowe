import timeit
import unittest
from random import randint

from entities.School import School

school = School("Name", "Address")


class Testing(unittest.TestCase):
    def testAddSubjects(self):
        def subFunc():
            for i in range(1000):
                school.addSubject("Subject" + str(i), 1, 12)

        print(timeit.timeit(subFunc, number=1))

    def testAddTeacher(self):
        def subFunc():
            for i in range(1000):
                school.addTeacher("Teacher" + str(i), "Teacher" + str(i), 22, 2000)

        print(timeit.timeit(subFunc, number=1))

    def testAddStudent(self):
        def subFunc():
            for i in range(1000):
                school.addStudent("Student_" + str(i), "Student_" + str(i), 12, 6, [])

        print(timeit.timeit(subFunc, number=1))

    def testAddGrade(self):
        def subFunc():
            for i in range(1000):
                school.addStudent("Student2" + str(i), "Student2" + str(i), 12, 6, [])

            for i in range(1000):
                school.addTeacher("Teacher_" + str(i), "Teacher_" + str(i), 22, 2000)

            for i in range(1000):
                school.addSubject("Subject_" + str(i), 1, 12)

            students = list(school.getAllStudents())
            teachers = list(school.getAllTeachers())
            subjects = list(school.subjects)
            for i in range(1000):
                school.addGrade(students[i],
                                teachers[i],
                                subjects[i], randint(1, 5))

        print(timeit.timeit(subFunc, number=1))
