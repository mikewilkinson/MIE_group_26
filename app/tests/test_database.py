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

    def test_get_items_sum(self,items):
        """Test the sum of infection treatments with BNF codes 05"""
        # Sample data for testing
        sample_data = [
            {'BNF_code': '0501%', 'items': 10},
            {'BNF_code': '0502%', 'items': 15},
            {'BNF_code': '0503%', 'items': 5},
            {'BNF_code': '0604%', 'items': 20}] # Not starting with '05'

        # Test when there are items with BNF codes 05
        total_sum = self.db_mod.get_items_sum('05%')
        expected_sum = sum(item['items'] for item in sample_data if item['BNF_code'].startswith('05'))
        self.assertEqual(total_sum, expected_sum)

        # Test when there are no items with BNF codes 05
        total_sum_nonexistent = self.db_mod.get_items_sum('nonexistent_code')
        self.assertEqual(total_sum_nonexistent, 0)

    def test_percentage_of_infection_drugs(self):
        """Test the percentage of infection drugs as a percentage of all infection treatments"""
        # Sample data for testing
        sample_data = [
            {'BNF_code': '0501%', 'items': 10},
            {'BNF_code': '0502%', 'items': 15},
            {'BNF_code': '0503%', 'items': 5},
            {'BNF_code': '0604%', 'items': 20}]  # Not starting with '05'

        # Total sum of infection treatments
        infection_sum = self.db_mod.get_items_sum('05%')

        # Calculate percentages
        antibacterial_per = format(round(self.db_mod.get_items_sum('0501%') / infection_sum, 4) * 100, '.2f')
        antifungal_per = format(round(self.db_mod.get_items_sum('0502%') / infection_sum, 4) * 100, '.2f')
        antiviral_per = format(round(self.db_mod.get_items_sum('0503%') / infection_sum, 4) * 100, '.2f')
        antiprotozoal_per = format(round(self.db_mod.get_items_sum('0504%') / infection_sum, 4) * 100, '.2f')
        antihelmintics_per = format(round(self.db_mod.get_items_sum('0505%') / infection_sum, 4) * 100, '.2f')

        # Verify percentages
        self.assertEqual(antibacterial_per, '33.33', "Expected 33.33 for Antibacterial percentage")
        self.assertEqual(antifungal_per, '50.00', "Expected 50.00 for Antifungal percentage")
        self.assertEqual(antiviral_per, '16.67', "Expected 16.67 for Antiviral percentage")
        self.assertEqual(antiprotozoal_per, '0.00', "Expected 0.00 for Antiprotozoal percentage")
        self.assertEqual(antihelmintics_per, '0.00', "Expected 0.00 for Antihelmintics percentage")

class TestCreatinineClearance(unittest.TestCase):
    def test_clearance_male(self):
        """Test creatinine clearance calculation for male patients"""
        result = calculate_clearance('m', 40, 70, 1.2)
        expected = ((140 - 40) * 70) / (72 * 1.2)
        self.assertAlmostEqual(result['clearance'], expected)

    def test_clearance_female(self):
        """Test creatinine clearance calculation for female patients"""
        result = calculate_clearance('f', 40, 70, 1.2)
        expected = (((140 - 40) * 70) / (72 * 1.2)) * 0.85
        self.assertAlmostEqual(result['clearance'], expected)

if __name__ == "__main__":
    unittest.main()


