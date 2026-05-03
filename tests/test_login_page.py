import pytest
import allure

from config.constants import const
from config.parameters import param
from config.faker_settings import faker


@pytest.mark.ui
@pytest.mark.ui_login_page
def test_success_login(login, open_login_page):
    allure.dynamic.title('Success login')

    login.fill_username_field(param.standart_user[0])
    login.fill_password_field(param.standart_user[1])

    login.check_that_error_container_is_not_visible()

    login.press_login_button()

    login.check_url(const.catalog_url)


@pytest.mark.ui
@pytest.mark.ui_login_page
def test_unsuccess_login(login, open_login_page):
    allure.dynamic.title('Login with unregistered account')

    login.fill_username_field(faker.first_name())
    login.fill_password_field(faker.password())
    login.press_login_button()

    login.check_errors_in_fields(2)
    login.check_is_error_message_expected(const.incorrect_login_data)
    login.check_url(const.login_url)

    login.close_error_text_block()
    login.check_errors_are_not_visible()
    login.check_that_error_container_is_not_visible()


@pytest.mark.ui
@pytest.mark.ui_login_page
@pytest.mark.parametrize(
    'username, password, error_text',
    [
        ('', param.standart_user[1], const.missing_username),
        (param.standart_user[0], '', const.missing_password),
        ('', '', const.missing_username),
    ],
)
def test_missing_data(login, open_login_page, username, password, error_text):
    allure.dynamic.title(f'''Login with missing data.
                         Username = {username}, Password = {password}''')

    login.fill_username_field(username)
    login.fill_password_field(password)

    login.press_login_button()

    login.check_is_error_message_expected(error_text)
    login.check_url(const.login_url)


@pytest.mark.ui
@pytest.mark.ui_login_page
def test_blocked_user(login, open_login_page):
    allure.dynamic.title('Unsuccessful login for blocked user')

    login.fill_username_field(param.locked_user[0])
    login.fill_password_field(param.locked_user[1])

    login.press_login_button()

    login.check_is_error_message_expected(const.blocked_user)
    login.check_url(const.login_url)
