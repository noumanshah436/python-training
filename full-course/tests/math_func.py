import json
import math
import requests


def add(x, y=2):
    return x + y


def product(x, y=2):
    return x * y


class Math:
    def add(self, a, b):
        return a + b


class StudentDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            # load the JSON data into a Python dictionary using json.load() method.
            self.__data = json.load(json_file)

    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student

    def close(self):
        pass


class MathOperations:
    def calculate_square_root(self, value):
        return math.sqrt(value)


class WeatherService:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_weather(self, city):
        response = requests.get(f"{self.api_url}/weather?q={city}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to fetch weather data")
