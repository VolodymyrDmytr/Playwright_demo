from playwright.sync_api import Page, expect
from config.constants import const


class BasePage:

    def __intit__(self):
        self.page = Page()

    def go_to_page(self, url: str) -> None:
        """Open page

        Args:
            url (str): URL of a page
        """
        self.page.goto(url)

    def check_title(self) -> bool:
        """Check and return is page has required title
        Required title (in config/constants.py): page_title

        Returns:
            bool: True, if page has required title
        """
        expect(self.page).to_have_title(const.page_title)

    def check_url(self, url: str) -> bool:
        """Checks is actual url is matching given url

        Args:
            url (str): Expected page url

        Returns:
            bool: True, if URL of current page is matching expected
        """
        expect(self.page).to_have_url(url)
