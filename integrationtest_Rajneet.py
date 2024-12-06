import os
import pytest
import sys
import requests
from app import LAT, LON
from dotenv import load_dotenv

load_dotenv()

def test_weather_api():
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key is missing in the .env file")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={api_key}&units=metric&lang=en"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Integration test passed: Received OK status from OpenWeather API")

        json_data = response.json()
        required_fields = ['name', 'main', 'weather', 'wind', 'sys']
        
        for field in required_fields:
            if field not in json_data:
                print(f"Integration test failed: Missing '{field}' field in API response")
                return
        
        print("Integration test passed: All required fields present in API response")

    else:
        print(f"Integration test failed: Received {response.status_code} from OpenWeather API")

if __name__ == '__main__':
    test_weather_api()
