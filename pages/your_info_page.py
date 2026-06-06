from pages.base_page import BasePage
from config.locators import YourInfoLocators

from playwright.async_api import expect, Locator, Page
import allure


class YourInfoPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = YourInfoLocators(self.page)

    # Helping methods
    async def _locator_by_field_name(
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
            return self.locators.first_name_field
        elif data == 'Last name':
            return self.locators.last_name_field
        elif data == 'Postal code':
            return self.locators.postal_code_field

    # Actions

    @allure.step('Filling First name field: {data}')
    async def fill_first_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "First name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.locators.first_name_field
        await locator.fill(data)

    @allure.step('Filling Last name field: {data}')
    async def fill_last_name_field(
            self,
            data: str,
    ) -> None:
        """Filling "Last name" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.locators.last_name_field
        await locator.fill(data)

    @allure.step('Filling Postal code field: {data}')
    async def fill_postal_code_field(
            self,
            data: str,
    ) -> None:
        """Filling "Postal code" field on Your Info page

        Args:
            data (str): Text to be inputed
        """
        locator = self.locators.postal_code_field
        await locator.fill(data)

    @allure.step('Click Cancel button')
    async def press_cancel_button(self) -> None:
        """Pressing 'Cancel' button on Your Info page
        """
        locator = self.locators.cancel_button
        await locator.click()

    @allure.step('Click Continue button')
    async def press_continue_button(self) -> None:
        """Pressing 'Continue' button on Your Info page
        """
        locator = self.locators.continue_button
        await locator.click()

    @allure.step('Check are fields contain errors')
    async def check_error_icons_in_fields(
            self,
    ) -> bool:
        """Check`s is error icon are visible in expected field
        on Your Info page

        Returns:
            bool: True, if error icons are visible
        """
        for i in range(0, 3):
            await expect(
                self.locators.error_icons_in_fields(i)).to_be_visible()

    @allure.step('Check are fields do not contain errors')
    async def check_missing_error_icons_in_fields(
            self,
    ) -> bool:
        """Check`s is error icons are invisible in expected field on Your Info
        page

        Returns:
            bool: True, if error icons are invisible
        """
        for i in range(0, 3):
            await expect(
                self.locators.error_icons_in_fields(i)).not_to_be_visible()

    @allure.step('Checks is error text as expected. Expected: {data}')
    async def check_error_text(
            self,
            data: str,
    ) -> bool:
        """Check`s is error message as expected on Your Info page

        Args:
            data (str): Expected error message

        Returns:
            bool: True, if error text is as expected
        """
        locator = self.locators.error_massege
        await expect(locator).to_have_text(data)

    @allure.step('Closing error block')
    async def close_error_block(self) -> None:
        """Closing error massege block on Your Info page
        """
        locator = self.locators.close_error_message_button
        await locator.click()

    @allure.step('Checks is error block is closed')
    async def check_is_error_block_absent(self) -> bool:
        """Checks is error massege block is invisible on Your Info page

        Returns:
            bool: True, if block is invisible
        """
        locator = self.locators.close_error_message_button
        await expect(locator).not_to_be_visible()

    @allure.step('Checks is {field_name} contains {data}')
    async def check_data_in_field(
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
        await expect(locator).to_have_text(data)
