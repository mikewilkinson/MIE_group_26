"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
#from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')

    def test_get_unique_items(self):
        """Test that number of unique items returns correct value and value is less than or equal to total items"""
        self.assertEquals(self.db_mod.get_unique_items(), 13935)
        self.assertLessEqual(self.db_mod.get_unique_items, self.db_mod.get_total_number_items)

    def test_average_calculation(self):
        """Test that avergae calculation returns correct value"""
        self.assertAlmostEqual(self.db_mod.get_average_cost(), 76.22)

if __name__ == "__main__":
    unittest.main()