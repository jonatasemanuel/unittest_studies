import unittest
from city_function import city_country


class CityTestCase(unittest.TestCase):
    """Test for city_function.py"""
    def test_city_country(self):
        formatted = city_country('santiago','chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = city_country('santiago','chile', 5000000)
        self.assertEqual(formatted, 'Santiago, Chile - Population: 5000000')

unittest.main()
