import unittest
from unitz.converter import convert, UnitConversionError

class TestUnitzConverter(unittest.TestCase):

    def test_basic_length_conversion(self):
        self.assertAlmostEqual(convert(1, "meter", "foot"), 3.28084, places=4)

    def test_mass_conversion(self):
        self.assertAlmostEqual(convert(2, "kilogram", "pound"), 4.40925, places=4)

    def test_alias_support(self):
        self.assertAlmostEqual(convert(1000, "m", "km"), 1.0)
        self.assertAlmostEqual(convert(1, "lb", "g"), 453.592, places=3)

    def test_incompatible_units(self):
        with self.assertRaises(UnitConversionError):
            convert(1, "meter", "gram")

    def test_unsupported_unit(self):
        with self.assertRaises(UnitConversionError):
            convert(1, "banana", "meter")

if __name__ == "__main__":
    unittest.main()
