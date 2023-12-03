import unittest
from app import app

import unittest
#from app import app
from app.database.controllers import Database
from app.database.models import PrescribingData
from app import db
class Testsearchbox(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()
        self.app_context = app.app_context()
        self.app_context.push()
    def tearDown(self):
        """Run post each test."""
        self.app_context.pop()


    def test_BNF_Code(self):
        """Test search box using BNF_Code"""
        search_query='0603020T0AAACAC'
        result = Database.search_drug(self,search_query)
        print(result)
        self.mock_data = [
            ('0603020T0AAACAC','Prednisolone_Tab 5mg', 645, 32579, 0.40022856799471224)
        ]
        if result == self.mock_data:
            print("test_BNF_Code is True")
        else:
            print("test_BNF_Code is False")

    def test_BNF_Name(self):
        """Test search box using BNF_Name"""
        search_query='Maalox_Susp 195mg/220mg/5ml S/F'
        result = Database.search_drug(self,search_query)
        print(result)
        self.mock_data = [
            ('0101010G0BBABAB','Maalox_Susp 195mg/220mg/5ml S/F', 11, 16, 0.6441322314049588)
        ]
        if result == self.mock_data:
            print("test_BNF_Name is True")
        else:
            print("test_BNF_Name is False")

    
if __name__ == "__main__":
    unittest.main()
