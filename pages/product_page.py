from playwright.sync_api import expect, Page
import allure

from pages.base_page import BasePage
from config.locators import ProductLocators


class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ProductLocators(self.page)

    @allure.step('Check is product title is {data}')
    def check_product_title(
            self,
            data: str,
    ) -> bool:
        """Check`s is title on page match expected title on product`s page

        Args:
            data (str): expected title

        Returns:
            bool: True, if title is as expected
        """
        locator = self.locators.title
        expect(locator).to_have_text(data)

    @allure.step('Check is product description is {data}')
    def check_product_description(
            self,
            data: str,
    ) -> bool:
        """Check`s is description on page match expected description
        on product`s page

        Args:
            data (str): expected description

        Returns:
            bool: True, if description is as expected
        """
        locator = self.locators.description
        expect(locator).to_have_text(data)

    @allure.step('Check is product price is {data}')
    def check_product_price(
            self,
            data: str,
    ) -> bool:
        """Check`s is price on page match expected price on product`s page

        Args:
            data (str): expected price

        Returns:
            bool: True, if price is as expected
        """
        locator = self.locators.price
        expect(locator).to_have_text(data)

    @allure.step('Click Add To Card button')
    def click_add_to_card_button(
            self,
    ) -> None:
        """Click on "Add to card" or "Remove" button.
        It`s depends on it`s current state.
        on product`s page
        """
        locator = self.locators.add_button
        locator.click()

    @allure.step('Click Remove button')
    def click_remove_button(
            self,
    ) -> None:
        """Click on "Add to card" or "Remove" button.
        It`s depends on it`s current state.
        on product`s page
        """
        locator = self.locators.remove_button
        locator.click()

    @allure.step('Click Back To Products button')
    def click_back_to_products_button(
            self,
    ) -> None:
        """Click "Back to products" button on product`s page
        """
        locator = self.locators.back_button
        locator.click()
