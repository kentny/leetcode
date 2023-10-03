import unittest
from time_based_key_value_store import TimeMap

class MyTestCase(unittest.TestCase):
    def test_something(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)

        result = time_map.get("foo", 1)
        self.assertEqual(result, "bar")

        result = time_map.get("foo", 3)
        self.assertEqual(result, "bar")

        time_map.set("foo", "bar2", 4)

        result = time_map.get("foo", 4)
        self.assertEqual(result, "bar2")

        result = time_map.get("foo", 5)
        self.assertEqual(result, "bar2")


if __name__ == '__main__':
    unittest.main()
