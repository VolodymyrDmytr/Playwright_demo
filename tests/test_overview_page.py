import pytest
import allure

from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.ui_overview_page
def test_back_button(overview, open_overview_page):
    allure.dynamic.title('Click Back button')

    overview.click_cancel_button()
    overview.check_url(const.catalog_url)


@pytest.mark.ui
@pytest.mark.ui_overview_page
def test_finish_button(overview, open_overview_page):
    allure.dynamic.title('Click Finish button')

    overview.click_finish_button()
    overview.check_url(const.done_url)


@pytest.mark.ui
@pytest.mark.ui_overview_page
def test_check_products(overview, open_overview_page):
    allure.dynamic.title('Check products data')

    for i in range(len(param.products)-1):
        overview.check_product_card(
            i,
            1,
            param.products[i]['title'],
            param.products[i]['description'],
            param.products[i]['price'],
        )


@pytest.mark.ui
@pytest.mark.ui_overview_page
def test_go_to_product(overview, open_overview_page):
    allure.dynamic.title('Click product link')

    for i in range(len(param.products)-1):
        overview.click_on_product(param.products[i]['title'])
        overview.check_url(const.product_url(param.products[i]['id']))
        overview.sys_back()


@pytest.mark.ui
@pytest.mark.ui_overview_page
def test_prices(overview, open_overview_page):
    allure.dynamic.title('Check Products price, Taxes, and Total price')
    overview.check_prices()
