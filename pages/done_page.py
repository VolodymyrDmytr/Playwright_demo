from pages.base_page import BasePage

from playwright.sync_api import expect
from config.locators import done_locators


class DonePage(BasePage):

    def __init__(self):
        super().__init__()

    # Actions

    def click_back_to_home_button(self) -> None:
        """Click`s on "Back Home" button on Done page
        """
        locator = done_locators.back_home_button
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
        locator = done_locators.page_title
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
        locator = done_locators.page_text
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
        locator = done_locators.image
        expect(locator).to_have_attribute('alt', data)
