import unittest
import math

# Custom implementation of hypot function
def custom_hypot(x, y):
    # Ensure that both x and y are numbers
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return math.sqrt(x * x + y * y)


class TestHypotFunction(unittest.TestCase):
    # Existing tests...

    def test_hypot_with_string(self):
        with self.assertRaises(ValueError):
            custom_hypot("3", 4)

    def test_hypot_with_list(self):
        with self.assertRaises(ValueError):
            custom_hypot([3], 4)

    def test_hypot_with_none(self):
        with self.assertRaises(ValueError):
            custom_hypot(None, 4)


if __name__ == "__main__":
    unittest.main()
