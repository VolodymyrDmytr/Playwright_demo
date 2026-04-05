from playwright.sync_api import expect, Page

from pages.base_page import BasePage
from config.locators import CartLocators


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CartLocators(self.page)

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
        locator = self.locators.card.nth(number)

        title_locator = self.locators.card_title(locator)
        description_locator = self.locators.card_description(locator)
        price_locator = self.locators.card_price(locator)

        expect(title_locator).to_have_text(title)
        expect(description_locator).to_have_text(description)
        expect(price_locator).to_have_text(price)

    def click_remove_button(
            self,
            number: int,
    ) -> None:
        """Clicks "Remove" button for a specific card on Cart page

        Args:
            number (int): Card`s number
        """
        locator = self.locators.card.nth(number - 1)
        self.locators.card_button(locator).click()

    # def change_product_amount(
    #         self,
    #         number: int,
    #         data: int,
    # ) -> None:
    #     """Change amount of a specific product in the cart on Cart page

    #     Args:
    #         number (int): card number
    #         data (int): amount of products
    #     """
    #     number -= 1
    #     locator = self.card.nth(number)
    #     self.card_amount(locator).fill(data)

    def click_continue_shopping_button(self) -> None:
        """Clicks "Continue shopping" button on Card page
        """
        locator = self.locators.continue_shopping_button
        locator.click()

    def click_checkout_button(self) -> None:
        """Clicks "Checkout" button on Card page
        """
        locator = self.locators.checkout_button
        locator.click()
