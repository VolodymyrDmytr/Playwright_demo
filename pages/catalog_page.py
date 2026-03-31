from playwright.sync_api import expect

from pages.base_page import BasePage
from config.locators import catalog_locators


class CatalogPage(BasePage):

    def __init__(self):
        super().__init__()

    def check_product_card(
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
        number -= 1
        locator = catalog_locators.product_card.nth(number)

        title_locator = catalog_locators.product_title(locator)
        description_locator = catalog_locators.product_description(locator)
        price_locator = catalog_locators.product_price(locator)
        image_locator = catalog_locators.product_image(locator)

        expect(title_locator).to_have_text(title)
        expect(description_locator).to_have_text(description)
        expect(price_locator).to_have_text(price)
        expect(image_locator).to_have_attribute('alt', title)

    def click_card_button(
            self,
            data: int,
    ) -> None:
        """Clicks "Add to card"/"Remove" button for specific card.
        Attention! If one of the card has "Remove" button,
        card number should be different

        Args:
            data (int): number of the card to be added to cart
        """
        data -= 1
        locators = catalog_locators.product_card.nth(data)
        catalog_locators.product_button(locators).click()

    def choose_sort(
            self,
            data: str,
    ) -> None:
        """Select option for sorting products

        Args:
            data (str): Should be available sort type
        """
        locator = catalog_locators.sort_select
        locator.select_option(value=data)
