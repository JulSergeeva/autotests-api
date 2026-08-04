import pytest

@pytest.fixture(scope="session")
def session_fixture():
    print("\n[SETUP] session_fixture")
    yield
    print("\n[TEARDOWN] session_fixture")

@pytest.fixture(scope="module")
def module_fixture():
    print("\n[SETUP] module_fixture")
    yield
    print("\n[TEARDOWN] module_fixture")

@pytest.fixture(scope="function")
def function_fixture():
    print("\n[SETUP] function_fixture")
    yield
    print("\n[TEARDOWN] function_fixture")

def test_one(session_fixture, module_fixture, function_fixture):
    print("Executing test_one")

def test_two(session_fixture, module_fixture, function_fixture):
    print("Executing test_two")

class TestClass:
    def test_three(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_three")

    def test_four(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_four")
