from playwright.sync_api import expect

from pages.base_page import BasePage
from config.locators import login_locators


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()

    def fill_username_field(
            self,
            data: str,
    ) -> None:
        """Fill username field

        Args:
            data (str): Username
        """
        locator = login_locators.username_field
        locator.fill(data)

    def fill_password_field(
            self,
            data: str,
    ) -> None:
        """Fill password field

        Args:
            data (str): Password
        """
        locator = login_locators.password_field
        locator.fill(data)

    def press_login_button(self) -> None:
        """Clicks Login button
        """
        locator = login_locators.login_button
        locator.click()

    def check_that_error_container_is_not_visible(self) -> bool:
        """Checks is error container is not visible
        *Don`t require asset

        Returns:
            bool: True, if error container is not visible. False, otherwise
        """
        locator = login_locators.error_message
        expect(locator).to_be_hidden()

    def check_is_error_message_expected(
            self,
            data: str,
    ) -> bool:
        """_summary_
        *Don`t require asset

        Args:
            data (str): required error message

        Returns:
            bool: True, if error text is matches expectations. False otherwise
        """
        locator = login_locators.error_message
        expect(locator).to_have_text(data)
