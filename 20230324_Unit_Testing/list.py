class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_constructor(self):
        self.list.get_data()
        self.assertEqual(self.list.get_data(), [1, 2, 3, 4, 5])

    def test_string_in_constructor(self):
        test_list = IntegerList("1", 2, "3", 4, 5, "6")
        self.assertEqual(test_list.get_data(), [2, 4, 5])

    def test_empty_list_constructor(self):
        test_list = IntegerList()
        self.assertEqual(test_list.get_data(), [])

    def test_get_data(self):
        self.assertEqual(self.list.get_data(), [1, 2, 3, 4, 5])

    def test_get_index(self):
        self.assertEqual(self.list.get_data(), [1, 2, 3, 4, 5])

    def test_valid_add_operation(self):
        self.list.add(6)
        self.assertEqual(self.list.get_data(), [1, 2, 3, 4, 5, 6])

    def test_invalid_add_operation(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("papaya")
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_valid_remove_index_operation(self):
        self.list.remove_index(2)
        self.assertEqual(self.list.get_data(), [1, 2, 4, 5])

    def test_invalid_remove_index_operation(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(12)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_get_valid_index(self):
        test_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(test_list.get(1), 2)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(12)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_valid_insert(self):
        self.list.insert(0, 1)
        self.assertEqual(self.list.get_data(), [1, 1, 2, 3, 4, 5])

    def test_invalid_index_insert(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(12, 1)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_invalid_element_insert(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "papaya")
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.list.get_biggest(), 5)

    def test_get_index(self):
        self.assertEqual(self.list.get_index(2), 1)


if __name__ == "__main__":
    unittest.main()
