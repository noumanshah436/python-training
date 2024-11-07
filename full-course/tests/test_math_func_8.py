from unittest import mock


# mock.patch.object (Mocking Object Methods or Attributes)

# mock.patch.object is used to mock methods or attributes of an object during the test.
# This is useful when you need to isolate a piece of functionality, preventing a method or attribute from performing its actual operation (e.g., API calls, database interactions, etc.).


class WeatherService:
    def get_temperature(self, city):
        # Imagine this makes an external API call to fetch weather data
        return 30  # Simulate a temperature


# Use the decorator to mock 'get_temperature' method
@mock.patch.object(WeatherService, 'get_temperature', return_value=25)
def test_get_temperature(mock_get_temperature):
    service = WeatherService()

    # Call the method, which will return the mocked value
    result = service.get_temperature("Lahore")

    # Assertions
    assert result == 25  # The mocked value is returned, not the actual one
    # Ensure it was called with the right city
    mock_get_temperature.assert_called_once_with("Lahore")


# *****************************

# Explanation:

# ->  @mock.patch.object(WeatherService, 'get_temperature', return_value=25)

# This decorator is used to mock the get_temperature method of the WeatherService class.
# The patch.object method allows us to replace the actual get_temperature method with a mocked version that will return a predefined value (25 in this case) whenever it is called, regardless of the input.
# The return_value=25 argument tells the mock to return 25 whenever get_temperature is called during the test.

# *****************

# -> mock_get_temperature:
# This is the mock version of the get_temperature method, which is automatically passed as an argument to the test function (test_get_temperature).



# *****************************

# run test:
# pytest test_math_func_8.py -v
