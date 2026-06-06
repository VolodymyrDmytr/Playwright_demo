from playwright.async_api import expect, Page
import logging
import allure

from pages.base_page import BasePage
from config.locators import CartLocators

logger = logging.getLogger(__name__)


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CartLocators(self.page)

    @allure.step("""Expected card {number} data:
                 Product amount: {amount}
                 Title: {title}
                 Description: {description}
                 Price: {price}""")
    async def check_cart_card(
            self,
            number: int,
            amount: int,
            title: str,
            description: str,
            price: str,
    ) -> bool:
        """Check data in the card on Cart page

        Args:
            number (int): card number
            amount (int): product amount in the cart
            title (str): product`s title
            description (str): product`s description
            price (str): product`s price

        Returns:
            bool: True, if data matches expectations
        """
        locator = self.locators.card.nth(number)

        title_locator = self.locators.card_title(locator)
        amount_locator = self.locators.card_amount(locator)
        description_locator = self.locators.card_description(locator)
        price_locator = self.locators.card_price(locator)

        logger.debug(
            """
            Actual: %s, %s, %s, %s, %s
            Expected: %s, %s, %s, %s, %s
            """,
            number, title_locator.text_content(),
            amount_locator.text_content(), description_locator.text_content(),
            price_locator.text_content(),
            number, title, amount, description, price,
        )

        await expect(title_locator).to_have_text(title)
        await expect(amount_locator).to_have_text(str(amount))
        await expect(description_locator).to_have_text(description)
        await expect(price_locator).to_have_text(price)

    @allure.step('Check that there are no cards on page')
    async def check_no_cards(self) -> bool:
        """Checks cards if cards are present on the Cart page

        Returns:
            bool: True, if cards are not present (visible)
        """
        locator = self.locators.card
        await expect(locator).not_to_be_visible()

    @allure.step('Pressing remove button for card #{number}')
    async def click_remove_button(
            self,
            number: int,
    ) -> None:
        """Clicks "Remove" button for a specific card on Cart page

        Args:
            number (int): Card`s number
        """
        locator = self.locators.card.nth(number - 1)
        await self.locators.card_button(locator).click()

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

    @allure.step('Click Continue Shopping button')
    async def click_continue_shopping_button(self) -> None:
        """Clicks "Continue shopping" button on Card page
        """
        locator = self.locators.continue_shopping_button
        await locator.click()

    @allure.step('Click Checkout button')
    async def click_checkout_button(self) -> None:
        """Clicks "Checkout" button on Card page
        """
        locator = self.locators.checkout_button
        await locator.click()
