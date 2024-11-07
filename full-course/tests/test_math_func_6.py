# test_math_operations.py
import unittest
from unittest.mock import Mock, patch

import pytest
from math_func import MathOperations, WeatherService

# Mocking in Python is often done with the unittest.mock module, which allows you to replace parts of your code with mock objects during tests.

# function-based test

# Mock 'math.sqrt' function in math_func file/module


@patch('math_func.math.sqrt')
def test_calculate_square_root(mock_sqrt):
    # Set the return value of the mocked function
    mock_sqrt.return_value = 5.0

    # Instantiate MathOperations and call calculate_square_root
    math_operations = MathOperations()
    result = math_operations.calculate_square_root(25)

    # Assertions
    mock_sqrt.assert_called_once_with(25)  # Ensure it was called with 25
    assert result == 5.0  # Check if result matches mock's return value

# Explanation:

# @patch('math_func.math.sqrt'):

# This is the patch decorator from the unittest.mock module. It replaces `math.sqrt` with a mock object for the duration of the test.
# The argument 'math_func.math.sqrt' specifies the path to the sqrt function in the math_func module. This is necessary because the mock needs to be applied to the exact location where sqrt is imported or used.
# The `mock_sqrt` parameter is the mock object that is passed into the test function. You can interact with this mock as needed.


# ********************************************

# class based test
class TestMathOperations(unittest.TestCase):
    # Mock 'math.sqrt' function in math_func file/module
    @patch('math_func.math.sqrt')
    def test_calculate_square_root(self, mock_sqrt):
        # Set the return value of the mocked function
        mock_sqrt.return_value = 5.0

        # Instantiate MathOperations and call calculate_square_root
        math_operations = MathOperations()
        result = math_operations.calculate_square_root(25)

        # Assertions
        mock_sqrt.assert_called_once_with(25)  # Ensure it was called with 25
        # Check if result matches mock's return value
        self.assertEqual(result, 5.0)


# ****************************************************************************************
# Mocking example using WeatherService:

# we will mock get method of requests module
# ****************************************************************************************

# class based mocking example

class TestWeatherService(unittest.TestCase):
    @patch('math_func.requests.get')  # Mock 'requests.get' function
    def test_get_weather_success(self, mock_get):
        # Create a mock response object with expected JSON data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 23.5}
        }
        mock_get.return_value = mock_response

        # Instantiate WeatherService and call get_weather
        service = WeatherService(api_url="http://fakeapi.com")
        result = service.get_weather("Lahore")

        # Assertions
        mock_get.assert_called_once_with("http://fakeapi.com/weather?q=Lahore")
        self.assertEqual(result["main"]["temp"], 23.5)
        self.assertEqual(result["weather"][0]["description"], "clear sky")

    @patch('math_func.requests.get')
    def test_get_weather_failure(self, mock_get):
        # Mock response with a failure status code
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Instantiate WeatherService and check for exception
        service = WeatherService(api_url="http://fakeapi.com")
        with self.assertRaises(ValueError):
            service.get_weather("UnknownCity")

        # Assert that the request was made with the expected URL
        mock_get.assert_called_once_with(
            "http://fakeapi.com/weather?q=UnknownCity")


# function-based mocking example


@patch('math_func.requests.get')
def test_get_weather_success(mock_get):
    # Create a mock response object with expected JSON data
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 23.5}
    }
    mock_get.return_value = mock_response

    # Instantiate WeatherService and call get_weather
    service = WeatherService(api_url="http://fakeapi.com")
    result = service.get_weather("Lahore")

    # Assertions
    mock_get.assert_called_once_with("http://fakeapi.com/weather?q=Lahore")
    assert result["main"]["temp"] == 23.5
    assert result["weather"][0]["description"] == "clear sky"


def test_get_weather_failure():
    with patch('math_func.requests.get') as mock_get:
        # Mock response with a failure status code
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Instantiate WeatherService and check for exception
        service = WeatherService(api_url="http://fakeapi.com")
        with pytest.raises(ValueError):
            service.get_weather("UnknownCity")

        # Assert that the request was made with the expected URL
        mock_get.assert_called_once_with(
            "http://fakeapi.com/weather?q=UnknownCity")


# ********************************************

# run test:

# pytest test_math_func_6.py -v
