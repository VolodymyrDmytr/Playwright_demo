from playwright.async_api import expect, Page
import allure
import logging

from pages.base_page import BasePage
from config.locators import CatalogLocators

logger = logging.getLogger('Catalog page')


class CatalogPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CatalogLocators(self.page)

    @allure.step("""Expected card {number} to have data:
                Title: {title}
                Description: {description}
                Price: {price}""")
    async def check_product_card(
            self,
            number: int,
            title: str,
            description: str,
            price: str,
    ) -> bool:
        """Checks data on product card

        Args:
            number (int): products card number in list
            title (str): product`s expected title
            description (str): product`s expected description
            price (str): product`s expected price (format - $0.00)

        Returns:
            bool: True, if all data correspond to expected one
        """
        locator = self.locators.product_card.nth(number)

        title_locator = self.locators.product_title(locator)
        description_locator = self.locators.product_description(locator)
        price_locator = self.locators.product_price(locator)
        image_locator = self.locators.product_image(locator)

        logger.debug(
            """
            Actual: %s, %s, %s
            Expected: %s, %s, %s
            """,
            title_locator.text_content(), description_locator.text_content(),
            price_locator.text_content(), title, description, price,
        )

        await expect(title_locator).to_have_text(title)
        await expect(description_locator).to_have_text(description)
        await expect(price_locator).to_have_text(price)
        await expect(image_locator).to_have_attribute('alt', title)

    @allure.step('Click Add To Card button for card #{data}')
    async def click_card_button(
            self,
            data: int,
    ) -> None:
        """Clicks "Add to card"/"Remove" button for specific card.
        Attention! If one of the card has "Remove" button,
        card number should be different

        Args:
            data (int): number of the card to be added to cart
        """
        locators = self.locators.product_card.nth(data)
        await self.locators.product_button(locators).click()

    @allure.step('Select {data} sort')
    async def choose_sort(
            self,
            data: str,
    ) -> None:
        """Select option for sorting products

        Args:
            data (str): Should be available sort type
        """
        locator = self.locators.sort_select
        await locator.select_option(value=data)
