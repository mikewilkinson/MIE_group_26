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
from app import app
from app.database.controllers import Database


class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
       
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')
        

    def test_get_unique_items(self):
        """Test that number of unique items returns correct value"""
        
        self.assertEquals(self.db_mod.number_of_unique_items(), 13935)

    def test_get_prescribed_items_per_pct(self):
        """Test that prescribed items per PCT is not 0"""
        self.assertNotEqual(self.db_mod.get_prescribed_items_per_pct(), 0)

    def test_top_prescribed_item(self):
        """Test that max quantity percentage returns correct drug and percentage"""
        self.assertEqual(self.db_mod.max_quantity_percentage(),(0.14, 'Methadone HCl_Oral Soln 1mg/1ml S/F'))

    def test_average_calculation(self):
        """Test that avergae calculation returns correct value"""
        
        self.assertAlmostEqual(self.db_mod.agerage_cost(), 76.22)

    def test_get_items_sum(self):
        """Test the sum of infection treatments with BNF codes 05"""

        # Test when there are items with BNF codes 05
        
        total_sum = self.db_mod.get_items_sum('05%')
        self.assertEqual(total_sum, 238512)

    def test_percentage_of_infection_drugs(self):
        """Test the percentage of infection drugs as a percentage of all infection treatments"""
       

        # Total sum of infection treatments
        infection_sum = self.db_mod.get_items_sum('05%')

        # Calculate percentages
        antibacterial_per = format(round(self.db_mod.get_items_sum('0501%') / infection_sum, 4) * 100, '.2f')
        antifungal_per = format(round(self.db_mod.get_items_sum('0502%') / infection_sum, 4) * 100, '.2f')
        antiviral_per = format(round(self.db_mod.get_items_sum('0503%') / infection_sum, 4) * 100, '.2f')
        antiprotozoal_per = format(round(self.db_mod.get_items_sum('0504%') / infection_sum, 4) * 100, '.2f')
        antihelmintics_per = format(round(self.db_mod.get_items_sum('0505%') / infection_sum, 4) * 100, '.2f')

        # Verify percentages
        self.assertEqual(antibacterial_per, '82.25', "Expected 33.33 for Antibacterial percentage")
        self.assertEqual(antifungal_per, '5.22', "Expected 50.00 for Antifungal percentage")
        self.assertEqual(antiviral_per, '2.68', "Expected 16.67 for Antiviral percentage")
        self.assertEqual(antiprotozoal_per, '9.62', "Expected 0.00 for Antiprotozoal percentage")
        self.assertEqual(antihelmintics_per, '0.23', "Expected 0.00 for Antihelmintics percentage")


if __name__ == "__main__":
    unittest.main()


