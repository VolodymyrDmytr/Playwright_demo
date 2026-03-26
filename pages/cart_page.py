from playwright.sync_api import Page, expect, Locator

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.page = Page()

    # Locators

    # > parent locator
    @property
    def card(self) -> Locator:
        """Locator for all available product cards on Cart page

        Returns:
            Locator: all cards
        """
        return self.page.locator('.cart_item')

    # > daughter`s locators
    def card_title(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for title in a specific card on Cart page

        Args:
            data (Locator): card locator

        Returns:
            Locator: Title`s locator
        """
        return data.locator('.inventory_item_name')

    def card_description(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for description in a specific card on Cart page

        Args:
            data (Locator): card locator

        Returns:
            Locator: description`s locator
        """
        return data.locator('.inventory_item_desc')

    def card_price(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for price in a specific card on Cart page

        Args:
            data (Locator): card locator

        Returns:
            Locator: price`s locator
        """
        return data.locator('.item_pricebar')

    def card_button(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for "Remove" button in a specific card on Cart page

        Args:
            data (Locator): card locator

        Returns:
            Locator: button`s locator
        """
        return data.locator('.btn_secondary')

    def card_amount(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for "amount of product" field in a specific card on
        Cart page

        Args:
            data (Locator): card locator

        Returns:
            Locator: amount of product`s locator
        """
        return data.locator('.cart_quantity')

    # Actions
    def check_cart_card(
            self,
            number: int,
            title: str,
            description: str,
            price: str,
    ) -> bool:
        """Check data in the card on Cart page

        Args:
            number (int): card number
            title (str): product`s title
            description (str): product`s description
            price (str): product`s price

        Returns:
            bool: True, if data matches expectations
        """
        number -= 1
        locator = self.card.nth(number)

        title_locator = self.card_title(locator)
        description_locator = self.card_description(locator)
        price_locator = self.card_price(locator)

        expect(title_locator).to_have_text(title)
        expect(description_locator).to_have_text(description)
        expect(price_locator).to_have_text(price)

    def click_remove_button(self, number: int) -> None:
        pass

    def change_product_amount(self, number: int, data: int) -> None:
        pass
