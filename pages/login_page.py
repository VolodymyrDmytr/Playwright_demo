from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.page = Page()

    # Indentificators
    @property
    def username_field(self):
        """Username field on login page

        Returns:
            it`s locator
        """
        return self.page.get_by_placeholder('Username')

    @property
    def password_field(self):
        """Password field on login page

        Returns:
            it`s locator
        """
        return self.page.get_by_placeholder('Password')

    @property
    def login_button(self):
        """Login button on login page

        Returns:
            it`s locator
        """
        return self.page.locator('input.submit-button')

    @property
    def error_message(self):
        """Block for errors on login page

        Returns:
            it`s locator
        """
        return self.page.locator('div.error-message-container')

    # Actions
    def fill_username_field(
            self,
            data: str,
    ) -> None:
        """Fill username field

        Args:
            data (str): Username
        """
        locator = self.username_field
        locator.fill(data)

    def fill_password_field(
            self,
            data: str,
    ) -> None:
        """Fill password field

        Args:
            data (str): Password
        """
        locator = self.password_field
        locator.fill(data)

    def press_login_button(self) -> None:
        """Clicks Login button
        """
        locator = self.login_button
        locator.click()

    def check_that_error_container_is_not_visible(self) -> bool:
        """Checks is error container is not visible
        *Don`t require asset

        Returns:
            bool: True, if error container is not visible. False, otherwise
        """
        locator = self.error_message
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
        locator = self.error_message
        expect(locator).to_have_text(data)
