"""
pytest is a popular testing framework for Python. It allows you to write and execute tests for your Python code. pytest simplifies the process of writing tests by providing a simple and intuitive API.

To use pytest, you need to follow these steps:
"""


# Installation: Install pytest using pip, which is the package manager for Python. Open your terminal or command prompt and run the following command:

# pip install pytest


# Write test functions: Create a Python file and define test functions using the test_ prefix. Each test function should perform some assertions to check the correctness of the code being tested. For example:

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

# Run tests: In the terminal, navigate to the directory containing your test file and run the following command:

# pytest


# pytest will automatically discover and execute all the test functions in the current directory and its subdirectories. It will display the test results, including the status (pass/fail) of each test.


"""
Additionally, pytest provides a rich set of features for testing, including fixtures, parameterization, test discovery, test skipping, and test coverage. You can customize and extend pytest according to your needs.

Here's a simple example that demonstrates the use of a fixture and parameterization in pytest:
"""

import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize("number", [1, 2, 3])
def test_even_number(numbers, number):
    assert number % 2 == 0

def test_sum(numbers):
    assert sum(numbers) == 15

"""
In this example, the numbers fixture returns a list of numbers, which is used by the other test functions. The test_even_number function is parameterized with different values of number, and pytest will execute the test for each parameter value.

pytest is a powerful and flexible testing framework that can greatly simplify the process of writing and running tests for your Python code. It is widely adopted and has an extensive ecosystem of plugins and integrations with other tools.
"""


# How to test if it is already installed?
# pytest --version
