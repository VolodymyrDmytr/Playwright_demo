import pytest
import allure

from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.ui_header
def test_open_navigation(header, open_catalog_page):
    allure.dynamic.title('Check navigation opening')

    header.open_navigation_menu()
    header.check_is_navigation_open(True)
    header.close_navigation_menu()
    header.check_is_navigation_open(False)


@pytest.mark.ui
@pytest.mark.ui_header
def test_navigation_all_items(header, open_catalog_page):
    allure.dynamic.title('Click All items link')

    product = param.get_random_product()

    header.click_on_product(product['title'])
    header.check_url(const.product_url(product['id']))

    header.open_navigation_menu()
    header.click_all_items_option()

    header.check_url(const.catalog_url)


@pytest.mark.ui
@pytest.mark.ui_header
def test_navigation_about(header, open_catalog_page):
    allure.dynamic.title('Click About link')

    header.open_navigation_menu()
    header.click_about_option()
    header.check_url(const.about_url)


@pytest.mark.ui
@pytest.mark.ui_header
def test_navigation_logout(header, open_catalog_page):
    allure.dynamic.title('Click Logout link')

    header.open_navigation_menu()
    header.click_log_out_option()
    header.check_url(const.login_url)


@pytest.mark.ui
@pytest.mark.ui_header
def test_navigation_reset_app_state(header, catalog, open_catalog_page):
    allure.dynamic.title('Click Reset app state link')

    for i in range(6):
        catalog.click_card_button(i)

    header.check_products_amount_in_the_cart(6)

    header.open_navigation_menu()
    header.click_reset_app_option()
    header.close_navigation_menu()

    header.check_url(const.catalog_url)
    header.check_products_amount_in_the_cart_is_not_visible()


@pytest.mark.ui
@pytest.mark.ui_header
def test_open_cart(header, open_catalog_page):
    allure.dynamic.title('Click Cart link')

    header.click_cart_icon()
    header.check_url(const.cart_url)
