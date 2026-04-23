from playwright.sync_api import Page, Locator


class UniversalLocators:

    def __init__(self, page: Page):
        self.page = page

    def locator_by_text(
        self,
        data: str,
    ) -> Locator:
        """Locator of a desired title (universal)

        Args:
            data (str): Product title

        Returns:
            Locator: Title's locator
        """
        return self.page.locator('.inventory_item_name').get_by_text(data)


class LoginLocators(UniversalLocators):

    @property
    def username_field(self) -> Locator:
        """Username field on login page

        Returns:
            it`s locator
        """
        return self.page.get_by_placeholder('Username')

    @property
    def password_field(self) -> Locator:
        """Password field on login page

        Returns:
            it`s locator
        """
        return self.page.get_by_placeholder('Password')

    @property
    def login_button(self) -> Locator:
        """Login button on login page

        Returns:
            it`s locator
        """
        return self.page.locator('input.submit-button')

    @property
    def error_message(self) -> Locator:
        """Block for errors on login page

        Returns:
            it`s locator
        """
        return self.page.locator('div.error-message-container')

    @property
    def close_error_button(self) -> Locator:
        """Locator for 'X' button in error message block
        *Needs to close the block

        Returns:
            Locator: It`s locator
        """
        return self.page.locator('.error-button')

    @property
    def error_in_field(self) -> Locator:
        """Locators for error icons in fields

        Returns:
            Locator: Locators for error icons
        """
        return self.page.locator('.error_icon')


class HeaderLocators(UniversalLocators):

    @property
    def burger_menu_button(self) -> Locator:
        """Burger menu button in Header

        Returns:
            it`s locator
        """
        return self.page.get_by_text('Open Menu')

    @property
    def close_navigation(self) -> Locator:
        """Close button button in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_text('Close Menu')

    @property
    def all_items_option_nav(self) -> Locator:
        """"All items" option in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_text('All Items')

    @property
    def about_option_nav(self) -> Locator:
        """"About" option in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_text('About')

    @property
    def log_out_option_nav(self) -> Locator:
        """"Log out" option in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_text('Logout')

    @property
    def reset_app_state_option_nav(self) -> Locator:
        """"Reset App State" option in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_text('Reset App State')

    @property
    def cart_icon(self) -> Locator:
        """Cart icon in Header

        Returns:
            it`s locator
        """
        return self.page.locator('.shopping_cart_link')

    @property
    def cart_bage(self) -> Locator:
        """Amount of products in the card bage on Cart icon on Catalog page

        Returns:
            Locator: It`s locator
        """
        return self.page.locator('.shopping_cart_badge')


class CartLocators(UniversalLocators):

    @property
    def continue_shopping_button(self) -> Locator:
        """"<- Continue Shopping" button on a cart page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.back')

    @property
    def checkout_button(self) -> Locator:
        """"Checkout" button on Cart page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.checkout_button')

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
        return data.locator('.inventory_item_price')

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


class CatalogLocators(UniversalLocators):

    @property
    def sort_select(self) -> Locator:
        """Sort select on Catalog page

        Returns:
            it`s locator
        """
        return self.page.locator('.product_sort_container')

    # Parent locator
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
        return data.locator('button')

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
        return data.locator('.inventory_item_img').locator('img')


class DoneLocators(UniversalLocators):

    @property
    def back_home_button(self) -> Locator:
        """"Back Home" button on Done page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.btn_primary')

    @property
    def image(self) -> Locator:
        """Success image on Done page

        Returns:
            Locator: Image`s locator
        """
        return self.page.locator('.pony_express')

    @property
    def page_title(self) -> Locator:
        """Title text on Done page

        Returns:
            Locator: Text`s locator
        """
        return self.page.locator('.complete-header')

    @property
    def page_text(self) -> Locator:
        """Text on Done page

        Returns:
            Locator: Text`s locator
        """
        return self.page.locator('.complete-text')


class OverviewLocators(UniversalLocators):

    @property
    def cancel_button(self) -> Locator:
        """"<- Cancel" button on a Overview page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.cart_cancel_link')

    @property
    def finish_button(self) -> Locator:
        """"Finish" button on Overview page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.btn_action')

    @property
    def items_total(self) -> Locator:
        """Item total locator on Overview page

        Returns:
            Locator: 2 strings of text in locator
        """
        return self.page.locator('.summary_subtotal_label')

    @property
    def tax(self) -> Locator:
        """Tax locator on Overview page

        Returns:
            Locator: 2 strings of text in locator
        """
        return self.page.locator('.summary_tax_label')

    @property
    def total_price(self) -> Locator:
        """Total price locator on Overview page

        Returns:
            Locator: 2 strings of text in locator
        """
        return self.page.locator('.summary_total_label')

    @property
    def delivery_method(self) -> Locator:
        """Shipping Information on Overview page

        Returns:
            Locator: 1 string in locator
        """
        return self.page.locator('.summary_value_label').nth(1)

    # > parent locator
    @property
    def card(self) -> Locator:
        """Locator for all available product cards on Overview page

        Returns:
            Locator: all cards
        """
        return self.page.locator('.cart_item')

    # > daughter`s locators
    def card_title(
        self,
        data: Locator,
    ) -> Locator:
        """Locator for title in a specific card on Overview page

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
        """Locator for description in a specific card on Overview page

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
        """Locator for price in a specific card on Overview page

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
        """Locator for "Remove" button in a specific card on Overview page

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
        Overview page

        Args:
            data (Locator): card locator

        Returns:
            Locator: amount of product`s locator
        """
        return data.locator('.cart_quantity')


class ProductLocators(UniversalLocators):

    @property
    def image(self) -> Locator:
        """Product`s image on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_img')

    @property
    def title(self) -> Locator:
        """Product`s title on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_desc')

    @property
    def description(self) -> Locator:
        """Product`s description on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_name')

    @property
    def price(self) -> Locator:
        """Product`s price on product`s page

        Returns:
            locator
        """
        return self.page.locator('.inventory_details_price')

    @property
    def button(self) -> Locator:
        """Add to card / Remove button on product`s page
        Depends on it`s current state. Because locator is for both

        Returns:
            locator
        """
        return self.page.locator('.btn_primary')

    @property
    def back_button(self) -> Locator:
        """"Back to products" button on product`s page
        Depends on it`s current state. Because locator is for both

        Returns:
            locator
        """
        return self.page.locator('.btn_secondary')


class YourInfoLocators(UniversalLocators):

    @property
    def first_name_field(self) -> Locator:
        """Locator of the "First Name" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder("First Name")

    @property
    def last_name_field(self) -> Locator:
        """Locator of the "Last Name" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder('Last Name')

    @property
    def postal_code_field(self) -> Locator:
        """Locator of the "Zip/Postal Code" field on Your Info Page

        Returns:
            Locator: Field`s locator
        """
        return self.page.get_by_placeholder('Zip/Postal Code')

    @property
    def cancel_button(self) -> Locator:
        """Locator of the "Cancel" button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.cart_cancel_link')

    @property
    def continue_button(self):
        """Locator of the "Continue" button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.submit-button')

    @property
    def error_massege(self) -> Locator:
        """Locator of the error message block on Your Info Page

        Returns:
            Locator: Block`s locator
        """
        return self.page.locator('.error-message-container')

    @property
    def close_error_message_button(self) -> Locator:
        """Locator of the error message close button on Your Info Page

        Returns:
            Locator: Button`s locator
        """
        return self.page.locator('.error-button')

    def error_icons_in_fields(
            self,
            data: int,
    ) -> Locator:
        """Locator of the error icon in fields on Your Info Page

        Args:
            data (int): Field number (0 - 2)

        Returns:
            Locator: Icon`s locator
        """
        return self.page.locator('.form_group').nth(data).locator(
            '.error_icon')
