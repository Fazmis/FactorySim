from core import Factory, Floor
import unittest

class TestFactory(unittest.TestCase):
    def setUp(self):
        self.factory = Factory()
        self.class_floor = Floor
        self.default_floor = Floor(0, (1, 1))


    # Test createfloor
    def test_createfloor_lenafter(self):
        self.factory.create_floor(area=(5, 2))
        self.assertEqual(len(self.factory.floors), 1)

    def test_createfloor_name(self):
        self.factory.create_floor((1, 1))
        self.assertEqual(self.factory.floors[0].name, f"Floor {self.factory.floor_id - 1}")
        self.factory.create_floor((1, 1), "abracadabra")
        self.assertEqual(self.factory.floors[1].name, f"abracadabra")


if __name__ == "__main__":
    unittest.main()