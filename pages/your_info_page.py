from pages.base_page import BasePage

from playwright.sync_api import expect, Locator


class YourInfoPage(BasePage):

    def __init__(self):
        super().__init__()

    # Locators

    @property
    def first_name_field(self) -> Locator:
        """Locator of the "First Name" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder('First Name')

    @property
    def last_name_field(self) -> Locator:
        """Locator of the "Last Name" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder('Last Name')

    @property
    def postal_code_field(self) -> Locator:
        """Locator of the "Zip/Postal Code" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder('Zip/Postal Code')

    @property
    def cancel_button(self) -> Locator:
        """Locator of the "Cancel" button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.cart_cancel_link')

    @property
    def continue_button(self):
        """Locator of the "Continue" button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.submit-button')

    @property
    def error_massege(self) -> Locator:
        """Locator of the error message block on Your Info Page

        Returns:
            Locator: Block`s locator
        """
        return self.page.locator('.error-message-container')

    @property
    def close_error_message_button(self) -> Locator:
        """Locator of the error message close button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.error-button')

    def error_icons_in_fields(
            self,
            data: Locator,
    ) -> Locator:
        """Locator of the error icon in fields on Your Info Page

        Args:
            data (Locator): Field`s locator

        Returns:
            Locator: Icon`s locator
        """
        return data.locator('.svg-inline--fa')

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
            return self.first_name_field
        elif data == 'Last name':
            return self.last_name_field
        elif data == 'Postal code':
            return self.postal_code_field

    # Actions

    def fill_first_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "First name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.first_name_field
        locator.fill(data)

    def fill_last_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "Last name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.last_name_field
        locator.fill(data)

    def fill_postal_code_field(
            self,
            data: str,
    ) -> None:
        """Filling "Postal code" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.postal_code_field
        locator.fill(data)

    def press_cancel_button(self) -> None:
        """Pressing 'Cancel' button on Your Info page
        """
        locator = self.cancel_button
        locator.click()

    def press_continue_button(self) -> None:
        """Pressing 'Continue' button on Your Info page
        """
        locator = self.continue_button
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

        expect(self.error_icons_in_fields(locator)).to_be_visible()

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
        locator = self.error_massege
        expect(locator).to_have_text(data)

    def close_error_block(self) -> None:
        """Closing error massege block on Your Info page
        """
        locator = self.close_error_message_button
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
