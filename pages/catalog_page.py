from playwright.sync_api import expect, Locator

from pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self):
        super().__init__()

    # identificators

    @property
    def sort_select(self) -> Locator:
        """Sort select on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator('.product_sort_container')

    # > Parent locator
    @property
    def product_card(self) -> Locator:
        """Locator for all available product cards on Catalog page

        Returns:
            Locator: Cards
        """
        return self.page.locator('.inventory_item')

    # > Daughter`s locators
    def product_button(
        self,
        data: Locator,
    ) -> Locator:
        """"Add to card" or "Remove" button on a specific card on Catalog page.
        Button which would be click depend`s on product`s state.

        Args:
            data (Locator): Card`s locator

        Returns:
            Locator: Button`s locator
        """
        return data.locator('.btn_secondary')

    def product_title(
        self,
        data: Locator,
    ) -> Locator:
        """Locator of Title on specific card on Catalog page

        Args:
            data (Locator): Card`s locator

        Returns:
            Locator: Title`s locator
        """
        return data.locator('.inventory_item_name')

    def product_description(
        self,
        data: Locator,
    ) -> Locator:
        """Locator of Description on specific card on Catalog page

        Args:
            data (Locator): Card`s locator

        Returns:
            Locator: Description`s locator
        """
        return data.locator('.inventory_item_desc')

    def product_price(
        self,
        data: Locator,
    ) -> Locator:
        """Locator of Price on specific card on Catalog page

        Args:
            data (Locator): Card`s locator

        Returns:
            Locator: Price`s locator
        """
        return data.locator('.inventory_item_price')

    def product_image(
        self,
        data: Locator,
    ) -> Locator:
        """Locator of Image on specific card on Catalog page

        Args:
            data (Locator): Card`s locator

        Returns:
            Locator: Image`s locator
        """
        return data.locator('.inventory_item_img')

    # Actions

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
        locator = self.product_card.nth(number)

        title_locator = self.product_title(locator)
        description_locator = self.product_description(locator)
        price_locator = self.product_price(locator)
        image_locator = self.product_image(locator)

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
        locators = self.product_card.nth(data)
        self.product_button(locators).click()

    def choose_sort(
            self,
            data: str,
    ) -> None:
        """Select option for sorting products

        Args:
            data (str): Should be available sort type
        """
        locator = self.sort_select
        locator.select_option(value=data)
