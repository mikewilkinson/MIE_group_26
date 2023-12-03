import unittest
from flask import Flask, request
from app.views.controllers import views, generate_data_for_tiles, generate_barchart_data, generate_infection_barchart_data
from app.database.controllers import Database
from sqlalchemy.sql import func,distinct


class TestDashboardViews(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(views)
        self.client = self.app.test_client()

    def test_home_route_get(self):
        response = self.client.get('/dashboard/home/')
        self.assertEqual(response.status_code, 500)

    def test_home_route_post(self):
        response = self.client.post('/dashboard/home/', data={'pct-option': 'example_pct'})
        self.assertEqual(response.status_code, 500)

    def test_generate_data_for_tiles(self):
        data = generate_data_for_tiles()
        self.assertIsInstance(data, list)

    def test_generate_barchart_data(self):
        data = generate_barchart_data()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertIsInstance(data[0], list)
        self.assertIsInstance(data[1], list)

    def test_generate_infection_barchart_data(self):
        data = generate_infection_barchart_data()
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)
        for key, value in data.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, str)

if __name__ == '__main__':
    unittest.main()