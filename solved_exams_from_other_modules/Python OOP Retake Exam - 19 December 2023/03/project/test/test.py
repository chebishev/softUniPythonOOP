from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobotClass(TestCase):
    def setUp(self):
        self.part = ClimbingRobot('Mountain', 'Arm', 100, 200)

    def test_climbing_robot_structure(self):
        self.assertEqual(ClimbingRobot.__base__.__name__, "object")
        self.assertTrue(hasattr(ClimbingRobot, "get_used_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_used_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "install_software"))

        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))

    def test_initialization(self):
        part = ClimbingRobot('Mountain', 'Arm', 100, 200)

        self.assertEqual(part.category, 'Mountain')
        self.assertEqual(part.part_type, 'Arm')
        self.assertEqual(part.capacity, 100)
        self.assertEqual(part.memory, 200)
        self.assertEqual(part.installed_software, [])

    def test_category_setter_valid(self):
        valid_categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        for category in valid_categories:
            with self.subTest(category=category):
                self.part.category = category
                self.assertEqual(self.part.category, category)

    def test_category_setter_invalid(self):
        invalid_category = 'InvalidCategory'
        with self.assertRaises(ValueError) as context:
            self.part.category = invalid_category
        self.assertEqual(str(context.exception), f"Category should be one of {self.part.ALLOWED_CATEGORIES}")

    def test_get_used_capacity(self):
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.part.installed_software = [software1, software2]
        self.assertEqual(self.part.get_used_capacity(), 70)

    def test_get_available_capacity(self):
        self.part.installed_software = [{'capacity_consumption': 30}]
        self.assertEqual(self.part.get_available_capacity(), 70)

    def test_get_used_memory(self):
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.part.installed_software = [software1, software2]
        self.assertEqual(self.part.get_used_memory(), 120)

    def test_get_available_memory(self):
        self.part.installed_software = [{'memory_consumption': 30}]
        self.assertEqual(self.part.get_available_memory(), 170)

    def test_install_software_success(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        result = self.part.install_software(software)
        self.assertEqual(result, f"Software '{software['name']}' successfully installed on {self.part.category} part.")
        self.assertEqual(self.part.installed_software, [software])

    def test_install_software_exact_capacity_memory(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption']
        self.part.memory = software['memory_consumption']

        result = self.part.install_software(software)

        expected_message = f"Software '{software['name']}' successfully installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [software])

    def test_install_software_memory_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption'] - 5
        self.part.memory = software['memory_consumption'] + 10

        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])

    def test_install_software_capacity_condition_only(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.part.installed_software = []
        self.part.capacity = software['capacity_consumption'] + 10
        self.part.memory = software['memory_consumption'] - 5

        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])

    def test_install_software_failure(self):
        software = {'name': 'Software1', 'capacity_consumption': 150, 'memory_consumption': 250}
        result = self.part.install_software(software)
        expected_message = f"Software '{software['name']}' cannot be installed on {self.part.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.part.installed_software, [])


if __name__ == '__main__':
    main()
