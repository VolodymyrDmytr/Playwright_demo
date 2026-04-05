import pytest

from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.ui_login_page
def test_success_login(login, open_login_page):
    login.fill_username_field('standard_user')
    login.fill_password_field(param.login_creds['standard_user'])
    login.press_login_button()

    login.check_url(const.catalog_url)
