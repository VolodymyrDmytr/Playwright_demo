from pages.base_page import BasePage
from config.locators import DoneLocators

from playwright.sync_api import expect, Page
import allure


class DonePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = DoneLocators(self.page)

    # Actions
    @allure.step('Click Back To Home button')
    def click_back_to_home_button(self) -> None:
        """Click`s on "Back Home" button on Done page
        """
        locator = self.locators.back_home_button
        locator.click()

    # Checks
    @allure.step('Check title on page. Expected: {data}')
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

    @allure.step('Check text on page. Expected: {data}')
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

    @allure.step('Check image on page (Its alt text). Expected: {data}')
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
