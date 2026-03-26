from playwright.sync_api import Page, expect, Locator
from config.constants import const


class BasePage:

    def __intit__(self):
        self.page = Page()

    # Locators

    def locator_by_text(
        self,
        data: str,
    ) -> Locator:
        """Locator of a desired title (universal)

        Args:
            data (str): Product title

        Returns:
            Locator: Title's locator
        """
        return self.page.get_by_text(data)

    # Actions

    def go_to_page(
            self,
            url: str,
    ) -> None:
        """Open page

        Args:
            url (str): URL of a page
        """
        self.page.goto(url)

    def check_page_title(self) -> bool:
        """Check and return is page has required title
        Required title (in config/constants.py): page_title

        Returns:
            bool: True, if page has required title
        """
        expect(self.page).to_have_title(const.page_title)

    def check_url(
            self,
            url: str,
    ) -> bool:
        """Checks is actual url is matching given url

        Args:
            url (str): Expected page url

        Returns:
            bool: True, if URL of current page is matching expected
        """
        expect(self.page).to_have_url(url)

    def click_on_product(
            self,
            data: str,
    ) -> None:
        """Clicks on product link by it`s name

        Args:
            data (str): name of product
        """
        locator = self.locator_by_text(data)
        locator.click()
