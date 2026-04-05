from pages.base_page import BasePage

from playwright.sync_api import expect, Page
from config.locators import DoneLocators


class DonePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DoneLocators(self.page)

    # Actions

    def click_back_to_home_button(self) -> None:
        """Click`s on "Back Home" button on Done page
        """
        locator = self.locators.back_home_button
        locator.click()

    # Checks

    def check_title(
            self,
            data: str,
    ) -> bool:
        """Check`s Title text on Done page

        Args:
            data (str): Expected title

        Returns:
            bool: True, if title text matches expected title
        """
        locator = self.locators.page_title
        expect(locator).to_have_text(data)

    def check_text(
            self,
            data: str,
    ) -> bool:
        """Check`s text on Done page

        Args:
            data (str): Expected text

        Returns:
            bool: True, if text matches expected text
        """
        locator = self.locators.page_text
        expect(locator).to_have_text(data)

    def check_image(
            self,
            data: str,
    ) -> bool:
        """Check`s image alt text on Done page

        Args:
            data (str): Expected Alt text

        Returns:
            bool: True, if alt matches expected alt
        """
        locator = self.locators.image
        expect(locator).to_have_attribute('alt', data)
