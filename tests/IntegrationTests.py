import unittest
from unittest.mock import patch
from datetime import datetime

from entities.School import School
from exceptions.ValidationException import ValidationException
from inputFuncs.functions import getInputDataForAddGrade


class TestIntegrationAddGrade(unittest.TestCase):
    def setUp(self):
        self.school = School("Test School", "Nowhere")
        self.subject = self.school.addSubject("Math", 1, 12)
        self.teacher = self.school.addTeacher("Smith", "John", 35, 4000)
        self.student = self.school.addStudent("Tom", "Doe", 14, 8, [])

    @patch("builtins.input", side_effect=[
        "Math",
        "Smith",
        "Doe",
        "5"
    ])
    @patch("builtins.print")
    def test_add_grade_integration(self, mock_print, mock_input):
        getInputDataForAddGrade(self.school)

        self.assertEqual(len(self.student.grades), 1)
        grade = self.student.grades[0]
        self.assertEqual(grade.subject, self.subject)
        self.assertEqual(grade.teacher, self.teacher)
        self.assertEqual(grade.grade, 5)

        mock_print.assert_any_call("Grade added successfully!")

    @patch("builtins.input", side_effect=[
        "Math",
        "Smith",
        "Doe",
        "6"
    ])
    def test_add_grade_invalid_mark(self, mock_input):
        with self.assertRaises(ValidationException) as context:
            getInputDataForAddGrade(self.school)

        self.assertEqual(str(context.exception), "Mark must be between 1 and 5!")
