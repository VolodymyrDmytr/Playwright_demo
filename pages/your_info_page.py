from pages.base_page import BasePage

from playwright.sync_api import expect, Locator
from config.locators import your_info_locators


class YourInfoPage(BasePage):

    def __init__(self):
        super().__init__()

    # Helping methods

    def _locator_by_field_name(
            self,
            data: str,
    ) -> Locator:
        """Help method to get locator by filed`s name on Your Info page

        Args:
            data (str): Options: First name / Last name / Postal code

        Returns:
            Locator: Field`s locator
        """
        if data == 'First name':
            return your_info_locators.first_name_field
        elif data == 'Last name':
            return your_info_locators.last_name_field
        elif data == 'Postal code':
            return your_info_locators.postal_code_field

    # Actions

    def fill_first_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "First name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = your_info_locators.first_name_field
        locator.fill(data)

    def fill_last_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "Last name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = your_info_locators.last_name_field
        locator.fill(data)

    def fill_postal_code_field(
            self,
            data: str,
    ) -> None:
        """Filling "Postal code" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = your_info_locators.postal_code_field
        locator.fill(data)

    def press_cancel_button(self) -> None:
        """Pressing 'Cancel' button on Your Info page
        """
        locator = your_info_locators.cancel_button
        locator.click()

    def press_continue_button(self) -> None:
        """Pressing 'Continue' button on Your Info page
        """
        locator = your_info_locators.continue_button
        locator.click()

    def check_error_icon_in_field(
            self,
            data: str,
    ) -> bool:
        """Check`s is error icon is visible in expected field on Your Info page

        Args:
            data (str): Options: First name / Last name / Postal code

        Returns:
            bool: True, if error icon is visible
        """
        locator = self._locator_by_field_name(data)

        expect(your_info_locators.error_icons_in_fields(locator)
               ).to_be_visible()

    def check_error_text(
            self,
            data: str,
    ) -> bool:
        """Check`s is error message as expected on Your Info page

        Args:
            data (str): Expected error message

        Returns:
            bool: True, if error text is as expected
        """
        locator = your_info_locators.error_massege
        expect(locator).to_have_text(data)

    def close_error_block(self) -> None:
        """Closing error massege block on Your Info page
        """
        locator = your_info_locators.close_error_message_button
        locator.click()

    def check_data_in_field(
            self,
            field_name: str,
            data: str,
    ) -> bool:
        """Check`s is data in the field is as expected on Your Info page

        Args:
            field_name (str): Options: First name / Last name / Postal code
            data (str): expected text in field

        Returns:
            bool: True, if text is as expected in a specific field
        """
        locator = self._locator_by_field_name(field_name)

        expect(locator).to_have_text(data)
