from playwright.sync_api import expect, Page

from pages.base_page import BasePage
from config.locators import LoginLocators


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = LoginLocators(self.page)

    def fill_username_field(
            self,
            data: str,
    ) -> None:
        """Fill username field on Login page

        Args:
            data (str): Username
        """
        locator = self.locators.username_field
        locator.fill(data)

    def fill_password_field(
            self,
            data: str,
    ) -> None:
        """Fill password field on Login page

        Args:
            data (str): Password
        """
        locator = self.locators.password_field
        locator.fill(data)

    def press_login_button(self) -> None:
        """Clicks Login button on Login page
        """
        locator = self.locators.login_button
        locator.click()

    def check_that_error_container_is_not_visible(self) -> bool:
        """Checks is error container is not visible on Login page
        *Don`t require asset

        Returns:
            bool: True, if error container is not visible. False, otherwise
        """
        locator = self.locators.error_message
        expect(locator).to_be_hidden()

    def check_is_error_message_expected(
            self,
            data: str,
    ) -> bool:
        """Check`s is message in error block matches expectations on Login page

        Args:
            data (str): required error message

        Returns:
            bool: True, if error text is matches expectations. False otherwise
        """
        locator = self.locators.error_message
        expect(locator).to_have_text(data)
