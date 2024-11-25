import unittest
import pytest
from app import app
from datetime import datetime

class TestWeatherAppDataTypes(unittest.TestCase):

    def setUpClass(cls):
        # Set up a test client for the Flask app
        cls.client = app.test_client()
        app.config['TESTING'] = True


    def test_update_weather_success_response(self): 
        # Test the structure and data types in a successful /update_weather response."""
        response = self.client.get('/update_weather')
        json_data = response.get_json()
        
        if response.status_code == 200:# Check if each field is present and has the correct type
        
            self.assertIsInstance(json_data['location'], str, "'location' should be a string")
            self.assertIsInstance(json_data['temperature'], (int, float), "'temperature' should be an integer or float")
            self.assertIsInstance(json_data['description'], str, "'description' should be a string")
            self.assertIsInstance(json_data['humidity'], int, "'humidity' should be an integer")
            self.assertIsInstance(json_data['wind_speed'], (int, float), "'wind_speed' should be an integer or float")
            self.assertIsInstance(json_data['sunrise'], str, "'sunrise' should be a string in 'HH:MM:SS' format")
            self.assertIsInstance(json_data['sunset'], str, "'sunset' should be a string in 'HH:MM:SS' format")
            try:
                datetime.strptime(json_data['sunrise'], '%H:%M:%S')
                datetime.strptime(json_data['sunset'], '%H:%M:%S')
            except ValueError:
                self.fail("Sunrise and sunset should be in 'HH:MM:SS' format")

        else:
            self.assertEqual(response.status_code, 500)
            self.assertIn('error', json_data)
            self.assertIsInstance(json_data['error'], str)

if __name__ == '__main__':
    unittest.main()
