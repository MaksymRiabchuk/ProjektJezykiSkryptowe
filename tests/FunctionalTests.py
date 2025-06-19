import unittest

from entities.School import isIntInRange, School

school = School("Name", "Address")


class Testing(unittest.TestCase):

    def test_addGrade(self):
        student = school.addStudent("Unknown", "Unknown", 12, 11, [])
        subject = school.addSubject("Unknown", 1, 12)
        teacher = school.addTeacher("Unknown", "Unknown", 24, 2000)
        grade = school.addGrade(student, teacher, subject, 5)
        assert grade is not None

    def test_updateGrade(self):
        student = school.addStudent("Unknown2", "Unknown2", 12, 11, [])
        subject = school.addSubject("Unknown2", 1, 12)
        teacher = school.addTeacher("Unknown2", "Unknown2", 24, 2000)
        grade = school.addGrade(student, teacher, subject, 5)
        assert grade is not None
        student.updateGradeWithTheSameDate(subject, teacher, 3)
        assert grade.grade == 3


if __name__ == '__main__':
    unittest.main()
