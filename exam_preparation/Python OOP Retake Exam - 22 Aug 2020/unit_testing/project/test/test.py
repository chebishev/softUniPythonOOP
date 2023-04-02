from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("John Doe", 1)

    def test_init(self):
        self.assertEqual(self.student_report_card.student_name, "John Doe")
        self.assertEqual(self.student_report_card.school_year, 1)

    def test_invalid_student_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("", 1)
        self.assertEqual(str(ve.exception), "Student Name cannot be an empty string!")

    def test_school_year_out_of_valid_range_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("John Doe", 13)
        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_add_grade_existing_subject(self):
        self.student_report_card.grades_by_subject["Maths"] = [5]
        self.student_report_card.add_grade("Maths", 5)
        self.assertEqual(self.student_report_card.grades_by_subject, {"Maths": [5, 5]})

    def test_add_grade_missing_subject(self):
        self.student_report_card.grades_by_subject["Maths"] = [5]
        self.student_report_card.add_grade("Chem", 2)
        self.assertEqual(self.student_report_card.grades_by_subject, {"Maths": [5], "Chem": [2]})

    def test_average_grade_by_subject(self):
        self.student_report_card.add_grade("Maths", 5)
        self.student_report_card.add_grade("Maths", 3)
        self.student_report_card.add_grade("Chem", 2)
        self.student_report_card.add_grade("Chem", 6)
        self.assertEqual(self.student_report_card.average_grade_by_subject(), "Maths: 4.00\nChem: 4.00")

    def test_average_grade_for_all_subjects(self):
        self.student_report_card.add_grade("Maths", 5)
        self.student_report_card.add_grade("Maths", 3)
        self.student_report_card.add_grade("Chem", 2)
        self.student_report_card.add_grade("Chem", 6)
        self.assertEqual(self.student_report_card.average_grade_for_all_subjects(), 'Average Grade: 4.00')

    def test__repr_method(self):
        self.student_report_card.add_grade("Maths", 5)
        self.student_report_card.add_grade("Maths", 3)
        self.student_report_card.add_grade("Chem", 2)
        self.student_report_card.add_grade("Chem", 6)
        self.assertEqual(self.student_report_card.__repr__(),
                         "Name: John Doe\n"
                         "Year: 1\n"
                         "----------\n"
                         "Maths: 4.00\n"
                         "Chem: 4.00\n"
                         "----------\n"
                         "Average Grade: 4.00")


if __name__ == "__main__":
    main()
