from unittest import TestCase
from horse_racings.project import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Bob", {"Math": ["Math 1", "Math 2"], "English": ["English 1", "English 2"]})
        self.student2 = Student("Paul")

    def test_initialization(self):
        self.assertEqual(self.student.name, "Bob")
        self.assertEqual(self.student.courses, {"Math": ["Math 1", "Math 2"], "English": ["English 1", "English 2"]})
        self.assertEqual(self.student2.name, "Paul")
        self.assertEqual(self.student2.courses, {})

    def test_enroll_already_added(self):
        self.assertEqual(self.student.enroll("Math", ["Math 3"]),
                         "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses, {"Math": ["Math 1", "Math 2", "Math 3"],
                                                "English": ["English 1", "English 2"]})

    def test_enroll_add_course_notes_empty(self):
        self.assertEqual(self.student.enroll("Chemistry", ["Chem 1"], add_course_notes=""),
                         "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"Math": ["Math 1", "Math 2"],
                                                "English": ["English 1", "English 2"],
                                                "Chemistry": ["Chem 1"]})

    def test_enroll_add_course_notes_Y(self):
        self.assertEqual(self.student.enroll("Chemistry", ["Chem 1"], add_course_notes="Y"),
                         "Course and course notes have been added.")
        self.assertEqual(self.student.courses, {"Math": ["Math 1", "Math 2"],
                                                "English": ["English 1", "English 2"],
                                                "Chemistry": ["Chem 1"]})

    def test_enroll_new_course_without_valid_course_notes(self):
        self.assertEqual(self.student2.enroll("Chemistry", ["Chem 1"], add_course_notes="N"), "Course has been added.")
        self.assertEqual(self.student2.courses, {"Chemistry": []})

    def test_add_notes_method(self):
        self.assertEqual(self.student.add_notes("Math", "Math 4"), "Notes have been updated")
        self.assertEqual(self.student.courses, {"Math": ["Math 1", "Math 2", "Math 4"],
                                                "English": ["English 1", "English 2"]})

    def test_add_notes_course_not_found(self):
        with self.assertRaises(Exception) as e:
            self.student.add_notes("Chemistry", "Chem 4")
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))

    def test_valid_leave_courese(self):
        self.assertEqual(self.student.leave_course("Math"), "Course has been removed")
        self.assertEqual(self.student.courses, {"English": ["English 1", "English 2"]})

    def test_leave_missing_course(self):
        with self.assertRaises(Exception) as e:
            self.student.leave_course("Chem")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))
