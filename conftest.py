from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.done_page import DonePage
from pages.header import Header
from pages.login_page import LoginPage
from pages.overview_page import OverviewPage
from pages.product_page import ProductPage
from pages.your_info_page import YourInfoPage

from playwright.sync_api import Page
import pytest
import logging
import allure

from config.logger_config import setup_logging
from config.constants import const
from config.parameters import param
from config.faker_settings import faker


logger = setup_logging()
logger = logging.getLogger(__name__)


@pytest.fixture()
def login(page: Page) -> object:
    """Fixture for Login page
    """
    yield LoginPage(page)


@pytest.fixture()
def catalog(page: Page) -> object:
    """Fixture for Catalog page
    """
    yield CatalogPage(page)


@pytest.fixture()
def product(page: Page) -> object:
    """Fixture for Product page
    """
    yield ProductPage(page)


@pytest.fixture()
def cart(page: Page) -> object:
    """Fixture for Cart page
    """
    yield CartPage(page)


@pytest.fixture()
def header(page: Page) -> object:
    """Fixture for Header
    """
    yield Header(page)


@pytest.fixture()
def your_info(page: Page) -> object:
    """Fixture for Your Info page
    """
    yield YourInfoPage(page)


@pytest.fixture()
def overview(page: Page) -> object:
    """Fixture for Overview page
    """
    yield OverviewPage(page)


@pytest.fixture()
def done(page: Page) -> object:
    """Fixture for Done page
    """
    yield DonePage(page)


@pytest.fixture()
def open_login_page(page: Page):
    """Fixture, for opening login page

    Args:
        page (Page): _description_
    """
    user = LoginPage(page)
    user.go_to_page(const.login_url)

    yield


@pytest.fixture()
def open_catalog_page(page: Page, open_login_page):
    user = LoginPage(page)

    user.fill_username_field(param.standart_user[0])
    user.fill_password_field(param.standart_user[1])

    user.press_login_button()

    user.check_url(const.catalog_url)

    yield


@pytest.fixture()
def open_cart_page_with_products(page: Page, open_catalog_page):
    catalog = CatalogPage(page)
    header = Header(page)

    for i in range(6):
        catalog.click_card_button(i)

    header.click_cart_icon()

    header.check_url(const.cart_url)

    yield


@pytest.fixture()
def open_your_info_page(page: Page, open_cart_page_with_products):
    cart = CartPage(page)
    cart.click_checkout_button()
    cart.check_url(const.checkout_1st_step_url)

    yield


@pytest.fixture()
def open_overview_page(page: Page, open_your_info_page):
    info = YourInfoPage(page)

    info.fill_first_name_field(faker.first_name())
    info.fill_last_name_field(faker.last_name())
    info.fill_postal_code_field(faker.postcode())

    info.press_continue_button()

    info.check_url(const.checkout_2nd_step_url)

    yield


@pytest.fixture()
def open_done_page(page: Page, open_overview_page):
    overview = OverviewPage(page)
    overview.click_finish_button()
    yield


# Allure fixture
@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request):
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name='failure_screenshot',
            attachment_type=allure.attachment_type.PNG
        )
