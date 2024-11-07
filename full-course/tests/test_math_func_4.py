from math_func import StudentDB
import pytest


# https://www.youtube.com/watch?v=JJmTO95AoqE&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=4


# We can use setup_module() method, which is called before a test method run and 
# teardown_module() method, which is called after a test method run.
# 
# pytest fixtures are pytest way of initializing and freeing the resources for all your tests.

# fixues are used to define all the variables or object, that we can use in our tests so that they are not recreated for each test.

@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db         # run the test and pass the args to the test function
    print('----------teardown----------------')
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'




# pytest test_math_func_4.py -v -s


# ***************************************

 
# Setup and Teardown with `pytest.fixture`**:

#    - `@pytest.fixture(scope='module')`: 
#       This decorator marks the `db` function as a fixture with a module-level scope. This means the `db` setup will be run once per module and shared across all tests in the file.
#      - **Purpose of Fixture**: Fixtures are used in `pytest` to handle setup and teardown logic, ensuring that resources are initialized before a test and cleaned up afterward.
#      - **Scope Parameter**: `scope='module'` means that the fixture will only be set up once before any test in the module is run, and it will be torn down once after all tests have run. 

#    - `db()` Function:
#      - Inside `db()`, `StudentDB()` is instantiated, and the `connect()` method is called to connect to `data.json`, the data file for student information.
#      - `yield db`: `yield` temporarily stops the function, allowing it to pass the `db` instance to the test functions. After all tests have run, the code resumes after `yield`, allowing teardown logic to execute.
#      - **Teardown Logic**: After the tests finish, `db.close()` is called to close the database connection, ensuring cleanup.
