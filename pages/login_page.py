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
        * Don`t require asset
        * Not visible == empty. Because block is always visible.

        Returns:
            bool: True, if error container is not visible. False, otherwise
        """
        locator = self.locators.error_message
        expect(locator).to_be_empty()

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

    def close_error_text_block(self) -> None:
        """Closing error block with text on Login page
        """
        locator = self.locators.close_error_button
        locator.click()

    def check_errors_in_fields(
            self,
            data: int,
    ) -> bool:
        """Checks that correct amount of fields have error icons in them

        Args:
            data (int): amount of fields that have error icons. Max 2

        Returns:
            bool: True, if expected amount matches expectations.
            False, otherwise
        """
        if data >= 3:
            return False
        elif data == 0:
            return False

        locator = self.locators.error_in_field
        assert locator.count() == data

    def check_errors_are_not_visible(self) -> bool:
        """Checks that errors in fields are not visible

        Returns:
            bool: True, if errors are hidden in the fields
        """
        locator = self.locators.error_in_field
        expect(locator).not_to_be_visible()
