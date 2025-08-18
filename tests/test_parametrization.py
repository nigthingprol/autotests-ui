import pytest
from _pytest.fixtures import SubRequest

# 1, 2, 3, -1

@pytest.mark.parametrize('number', [1, 2, -1, 3])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected',  [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of__numbers(os: str, browser: str):
    assert len(os+browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])                  
    def test_user_with_operation(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operation(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+79009898989': 'User with money on bank account',
    '+79009898981': 'User without money on bank account',
    '+79009898986': 'User with operations on bank account'
}


@pytest.mark.parametrize(
        'phone_number',
        users.keys(),
        ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...