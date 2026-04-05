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

from config.constants import const


@pytest.fixture(autouse=True)
def login(page: Page) -> object:
    """Fixture for Login page
    """
    yield LoginPage(page)


@pytest.fixture(autouse=True)
def catalog(page: Page) -> object:
    """Fixture for Catalog page
    """
    yield CatalogPage(page)


@pytest.fixture(autouse=True)
def product(page: Page) -> object:
    """Fixture for Product page
    """
    yield ProductPage(page)


@pytest.fixture(autouse=True)
def cart(page: Page) -> object:
    """Fixture for Cart page
    """
    yield CartPage(page)


@pytest.fixture(autouse=True)
def header(page: Page) -> object:
    """Fixture for Header
    """
    yield Header(page)


@pytest.fixture(autouse=True)
def your_info(page: Page) -> object:
    """Fixture for Your Info page
    """
    yield YourInfoPage(page)


@pytest.fixture(autouse=True)
def overview(page: Page) -> object:
    """Fixture for Overview page
    """
    yield OverviewPage(page)


@pytest.fixture(autouse=True)
def done(page: Page) -> object:
    """Fixture for Done page
    """
    yield DonePage(page)


@pytest.fixture(autouse=True)
def open_login_page(page: Page):
    """Fixture, for opening login page

    Args:
        page (Page): _description_
    """
    user = LoginPage(page)
    user.go_to_page(const.login_url)

    yield
