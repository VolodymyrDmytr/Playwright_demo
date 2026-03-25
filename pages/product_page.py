from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self):
        self.page = Page()

    # Identificators

    @property
    def image(self):
        """Product`s image on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_img')

    @property
    def title(self):
        """Product`s title on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_desc')

    @property
    def description(self):
        """Product`s description on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_name')

    @property
    def price(self):
        """Product`s price on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_price')

    @property
    def button(self):
        """Add to card / Remove button on product`s page
        Depends on it`s current state. Because locator is for both

        Returns:
            locator
        """
        return self.page.locator('.btn_primary')

    @property
    def back_button(self):
        """"Back to products" button on product`s page
        Depends on it`s current state. Because locator is for both

        Returns:
            locator
        """
        return self.page.locator('.btn_secondary')

    # Actions
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
        locator = self.title
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
        locator = self.description
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
        locator = self.price
        expect(locator).to_have_text(data)

    def click_status_button(
            self,
    ) -> None:
        """Click on "Add to card" or "Remove" button.
        It`s depends on it`s current state.
        on product`s page
        """
        locator = self.button
        locator.click()

    def click_back_to_products_button(
            self,
    ) -> None:
        """Click "Back to products" button on product`s page
        """
        locator = self.back_button
        locator.click()
