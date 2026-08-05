import pytest

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperation:
    def test_user_with_operations(self, user: str):
        print(f"{user} with operation")

    def test_user_without_operations(self, user: str):
        print(f"{user} without operation")


@pytest.mark.parametrize("phone_number", ["+700011000000", "+7334400000"], ids=["user with money", "user without money"])
def test_identifiers(phone_number: int):
    ...
