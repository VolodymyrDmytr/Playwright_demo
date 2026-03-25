from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self):
        self.page = Page()

    # identificators

    @property
    def add_to_cart_buttons(self):
        """"Add to cart" buttons on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator(
            'button',
            has_text='add-to-cart-sauce-labs-bolt-t-shirt')

    @property
    def remove_buttons(self):
        """"Remove" buttons on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator(
            'button',
            has_text='remove-sauce-labs-backpack')

    @property
    def product_cards(self):
        """Cards on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator('.inventory_item')

    @property
    def product_image_in_card(self):
        """Product images on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator('img.inventory_item_img')

    @property
    def sort_select(self):
        """Sort select on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator('.product_sort_container')

    # Actions

    def click_on_product(
            self,
            data: str,
    ) -> None:
        """Clicks on product link by it`s name

        Args:
            data (str): name of product
        """
        locator = self.page.get_by_text(data)
        locator.click()

    def check_product_card(
            self,
            number: int,
            data: dict,
    ) -> bool:
        """Checks data on product card

        Args:
            number (int): products card number in list

            data (dict): dict should contain next keys:
            title, description, price

        Returns:
            bool: _description_
        """
        number -= 1
        locator = self.product_cards.nth(number)
        img_locator = self.product_image_in_card.nth(number)

        expect(locator).to_have_text(data['title'])
        expect(locator).to_have_text(data['description'])
        expect(locator).to_have_text(data['price'])

        expect(img_locator).to_have_attribute('alt', data['title'])

    def click_add_to_card_button(
            self,
            data: int,
    ) -> None:
        """Clicks "Add to card" button for specific card.
        Attention! If one of the card has "Remove" button,
        card number should be different

        Args:
            data (int): number of the card to be added to cart
        """
        data -= 1
        locators = self.add_to_cart_buttons.nth(data)
        locators.click()

    def click_remove_button(
        self,
        data: int,
    ) -> None:
        """Clicks "Remove" button for specific card.
        Attention! If one of the card has "Add to card" button,
        card number should be different

        Args:
            data (int): number of the card to be removed from cart
        """
        data -= 1
        locators = self.remove_buttons.nth(data)
        locators.click()

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
