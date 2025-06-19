import unittest

from entities.School import School
from exceptions.ValidationException import ValidationException

school = School("Name", "Address")


class Testing(unittest.TestCase):

    def test_addStudent(self):
        with self.assertRaises(ValidationException) as context:
            school.addStudent("Unknown", "Unknown", 5, 11, [])

        self.assertEqual(str(context.exception), "Age must be a valid integer between 6 and 18")

    def test_addTeacher(self):
        with self.assertRaises(ValidationException) as context:
            school.addTeacher("Unknown", "Unknown", 19, 2000)

        self.assertEqual(str(context.exception), "Age of new teacher must be a number in range 20-60")

    def test_addSubject(self):
        with self.assertRaises(ValidationException) as context:
            school.addSubject("Unknown2", 0, 12)

        self.assertEqual(str(context.exception), "Start grade of subject must be a number in range 1-12")


if __name__ == '__main__':
    unittest.main()
