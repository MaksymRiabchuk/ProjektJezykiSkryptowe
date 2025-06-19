import unittest

from entities.School import isIntInRange, School

school = School("Name", "Address")


class Testing(unittest.TestCase):

    def test_isIntInRange_valid(self):
        assert isIntInRange(3, 5) is True

    def test_isIntInRange_invalid(self):
        assert isIntInRange(7, 5) is False

    def test_addStudent(self):
        student = school.addStudent("Unknown", "Unknown", 12, 11, [])
        assert student is not None
        school.people = []

    def test_checkStudent(self):
        assert school.checkStudent("Unknown", "Unknown") is False
        school.addStudent("Unknown", "Unknown", 12, 11, [])
        assert school.checkStudent("Unknown", "Unknown") is True

    def test_addSubject(self):
        subject = school.addSubject("Unknown", 1, 12)
        assert subject is not None
        school.subjects = []


if __name__ == '__main__':
    unittest.main()
