from pages.base_page import BasePage
from config.locators import HeaderLocators

from playwright.sync_api import Page, expect
import allure


class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HeaderLocators(self.page)

    @allure.step('Click on Burger menu')
    def open_navigation_menu(self) -> None:
        """Clicks on burger menu icon to open navigation
        """
        locator = self.locators.burger_menu_button
        locator.click()

    @allure.step('Close navigation menu')
    def close_navigation_menu(self) -> None:
        """Clicks on "X" in navigation to close it. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.close_navigation
        locator.click()

    @allure.step("Click 'All items' link in Nav menu")
    def click_all_items_option(self) -> None:
        """Clicks on "All items" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.all_items_option_nav
        locator.click()

    @allure.step("Click 'About' link in Nav menu")
    def click_about_option(self) -> None:
        """Clicks on "About" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.about_option_nav
        locator.click()

    @allure.step("Click 'Log out' link in Nav menu")
    def click_log_out_option(self) -> None:
        """Clicks on "Log out" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.log_out_option_nav
        locator.click()

    @allure.step("Click 'Reset App' link in Nav menu")
    def click_reset_app_option(self) -> None:
        """Clicks on "Reset App State" in navigation.
        Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.locators.reset_app_state_option_nav
        locator.click()

    @allure.step("Click Cart icon in Header")
    def click_cart_icon(self) -> None:
        """Clicks on the cart icon
        """
        locator = self.locators.cart_icon
        locator.click()

    @allure.step("Check that product amount in cart is {data} in Header")
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

    @allure.step('Checks that no product amount is shown in Header')
    def check_products_amount_in_the_cart_is_not_visible(
            self,
    ) -> bool:
        """Checks is amount of products in the cart is not visible in Header

        Returns:
            bool: True, if products amount is not visible
        """
        locator = self.locators.cart_bage
        expect(locator).not_to_be_visible()

    @allure.step('Checks that navigation menu is open')
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
