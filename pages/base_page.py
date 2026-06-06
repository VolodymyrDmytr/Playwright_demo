from playwright.async_api import Page, expect
import allure

from config.constants import const
from config.locators import UniversalLocators


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.locators = UniversalLocators(self.page)

    @allure.step('Open url: {url}')
    async def go_to_page(
            self,
            url: str,
    ) -> None:
        """Open page

        Args:
            url (str): URL of a page
        """
        await self.page.goto(url)

    @allure.step('Expected page title: {const.page_title}')
    async def check_page_title(self) -> bool:
        """Check and return is page has required title
        Required title (in config/constants.py): page_title

        Returns:
            bool: True, if page has required title
        """
        await expect(self.page).to_have_title(const.page_title)

    @allure.step('Expeced page url: {url}')
    async def check_url(
            self,
            url: str,
    ) -> bool:
        """Checks is actual url is matching given url

        Args:
            url (str): Expected page url

        Returns:
            bool: True, if URL of current page is matching expected
        """
        await expect(self.page).to_have_url(url)

    @allure.step('Click on product link: {data}')
    async def click_on_product(
            self,
            data: str,
    ) -> None:
        """Clicks on product link by it`s name

        Args:
            data (str): name of product
        """
        locator = self.locators.locator_by_text(data)
        await locator.click()

    @allure.step("Press system 'Back' button")
    async def sys_back(self) -> None:
        await self.page.go_back()
