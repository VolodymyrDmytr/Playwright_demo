from playwright.sync_api import expect

from pages.base_page import BasePage
from config.locators import product_locators


class ProductPage(BasePage):

    def __init__(self):
        super().__init__()

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
        locator = product_locators.title
        expect(locator).to_have_text(data)

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
        locator = product_locators.description
        expect(locator).to_have_text(data)

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
        locator = product_locators.price
        expect(locator).to_have_text(data)

    def click_status_button(
            self,
    ) -> None:
        """Click on "Add to card" or "Remove" button.
        It`s depends on it`s current state.
        on product`s page
        """
        locator = product_locators.button
        locator.click()

    def click_back_to_products_button(
            self,
    ) -> None:
        """Click "Back to products" button on product`s page
        """
        locator = product_locators.back_button
        locator.click()
