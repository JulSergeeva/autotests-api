from typing import Any
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    logger.info(f"Check that response status code is equal to {expected}")

    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """

    logger.info(f'Check that "{name}" equal to {expected}')

    assert actual == expected, (
        f'Incorrect value: "{name}".'
        f'Expected value: {expected}.'
        f'Actual value: {actual}'
    )

def assert_is_true(actual: Any, name: str):

    logger.info(f'Check that "{name}" equals is true')

    assert actual, (
        f'Incorrect value: "{name}".'
        f'Expected true value but got: {actual}'
    )
