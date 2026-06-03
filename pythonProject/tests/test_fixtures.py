import pytest

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Иницализация настроек автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def users_client():
    print("[FUNCTION] Создаем API Client на каждый автотест")

class TestUserFlow:
    def test_user_can_login(self, user, users_client):
        ...

    def test_user_can_create_course(self, user, users_client):
        ...

class TestAccountFlow:
    def test_user_account(self, user, users_client):
        ...


@pytest.fixture()
def user_data():
    return {"username": "test_user", "email": "test@test.ru"}

def test_user_email(user_data):
    assert user_data["email"] == "test@test.ru"

def test_user_name(user_data):
    assert user_data["username"] == "test_user"