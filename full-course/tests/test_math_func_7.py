import pytest
import asyncio

# require `pytest-asyncio` package to run asynchronous tests:
# pip install pytest-asyncio

# **********************************************

# 1. pytest.mark.asyncio (For Asynchronous Tests)

# When testing async code with pytest, you need to use pytest.mark.asyncio to tell pytest to run the test as an asynchronous function. 
# This is necessary because pytest doesn't natively know how to handle async def functions without this marker.

async def fetch_data():
    # Simulate an async operation (e.g., API call)
    await asyncio.sleep(1)
    return "data"

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == "data"



# **********************************************

# run test:
# pytest test_math_func_7.py -v

# I have created `pytest.ini` file for pytest configuration for running tests with asyncio support

# ***************************************

# Explanation:

# fetch_data is an async function that simulates fetching data (e.g., a network request).
# The test function test_fetch_data is marked with @pytest.mark.asyncio, indicating that it will run asynchronously.
# We use await to call fetch_data and check if it returns the expected result "data".