import allure
import pytest

from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.url
def test_login_page(login):
    allure.dynamic.title('Go to login page')
    login.go_to_page(const.login_url)
    login.check_url(const.login_url)


@pytest.mark.ui
@pytest.mark.url
@pytest.mark.parametrize('url, path', [
    (const.catalog_url, const.catalog_path),
    (const.cart_url, const.cart_path),
    (const.done_url, const.done_path),
    (const.checkout_1st_step_url, const.checkout_1st_step_url_path),
    (const.checkout_2nd_step_url, const.checkout_2nd_step_url_path),
    (const.product_url(param.get_random_product()['id']), const.product_path),
])
def test_access_to_pages(login, url, path):
    allure.dynamic.title(f'Try to go on {path} page, without login')
    login.go_to_page(url)
    login.check_url(const.login_url)

    expected_error_message = const.access_error_message(path)
    login.check_is_error_message_expected(expected_error_message)
