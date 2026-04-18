from pages.base_page import BasePage
from config.locators import HeaderLocators

from playwright.sync_api import Page, expect


class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HeaderLocators(self.page)

    def open_navigation_menu(self) -> None:
        """Clicks on burger menu icon to open navigation
        """
        locator = self.locators.burger_menu_button
        locator.click()

    def close_navigation_menu(self) -> None:
        """Clicks on "X" in navigation to close it. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.close_navigation
        locator.click()

    def click_all_items_option(self) -> None:
        """Clicks on "All items" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.all_items_option_nav
        locator.click()

    def click_about_option(self) -> None:
        """Clicks on "About" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.about_option_nav
        locator.click()

    def click_log_out_option(self) -> None:
        """Clicks on "Log out" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.log_out_option_nav
        locator.click()

    def click_reset_app_option(self) -> None:
        """Clicks on "Reset App State" in navigation.
        Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.reset_app_state_option_nav
        locator.click()

    def click_cart_icon(self) -> None:
        """Clicks on the cart icon
        """
        locator = self.locators.cart_icon
        locator.click()

    def check_products_amount_in_the_cart(
            self,
            data: int,
    ) -> bool:
        """Checks is amount of products in the cart is as expected in
        Header

        Args:
            data (int): Expected amount of products in the cart (max 6)

        Returns:
            bool: True, if actual products amount mathces expectations
        """
        data = str(data)
        locator = self.locators.cart_bage
        expect(locator).to_have_text(data)

    def check_products_amount_in_the_cart_is_not_visible(
            self,
    ) -> bool:
        """Checks is amount of products in the cart is not visible in Header

        Returns:
            bool: True, if products amount is not visible
        """
        locator = self.locators.cart_bage
        expect(locator).not_to_be_visible()

    def check_is_navigation_open(
            self,
            data: bool,
    ) -> bool:
        """Return bool, that depends on navigation state.
        *It looks on 'X' icon in navigation

        Args:
            data (bool): Navigation desirable state. True, if open

        Returns:
            bool: True, if navigation is in expected state
        """
        locator = self.locators.close_navigation
        if data is True:
            expect(locator).to_be_visible()
        elif data is False:
            expect(locator).not_to_be_visible()
