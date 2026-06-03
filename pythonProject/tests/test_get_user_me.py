from clients.authentication.authentication_client import AuthenticationClient
from clients.users.private_users_client import PrivateUsersClient
from tests.conftest import UserFixture


def test_get_user_me(private_users_client: PrivateUsersClient):
    ...