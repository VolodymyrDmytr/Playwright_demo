from playwright.sync_api import expect

from pages.base_page import BasePage
from config.locators import cart_locators


class CartPage(BasePage):

    def __init__(self):
        super().__init__()

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
        locator = cart_locators.card.nth(number)

        title_locator = cart_locators.card_title(locator)
        description_locator = cart_locators.card_description(locator)
        price_locator = cart_locators.card_price(locator)

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
        locator = cart_locators.card.nth(number - 1)
        cart_locators.card_button(locator).click()

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
        locator = cart_locators.continue_shopping_button
        locator.click()

    def click_checkout_button(self) -> None:
        """Clicks "Checkout" button on Card page
        """
        locator = cart_locators.checkout_button
        locator.click()
