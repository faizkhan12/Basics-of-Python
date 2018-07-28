import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Test for city_country.py"""
    def test_city_country(self):
        formatted_name=city_country('Santiago','Chile')
        self.assertEqual(formatted_name,'Santiago,Chile')

    def test_city_country_population(self):
        formatted_name=city_country('Santiago','Chile',population=100)
        self.assertEqual(formatted_name,'Santiago,Chile-population 100')

unittest.main()
