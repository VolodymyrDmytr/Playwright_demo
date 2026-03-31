from pages.base_page import BasePage
from config.locators import header_locators


class Header(BasePage):

    def __init__(self):
        super().__init__()

    def open_navigation_menu(self) -> None:
        """Clicks on burger menu icon to open navigation
        """
        locator = header_locators.burger_menu_button
        locator.click()

    def close_navigation_menu(self) -> None:
        """Clicks on "X" in navigation to close it. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = header_locators.close_navigation
        locator.click()

    def click_all_items_option(self) -> None:
        """Clicks on "All items" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = header_locators.all_items_option_nav
        locator.click()

    def click_about_option(self) -> None:
        """Clicks on "About" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = header_locators.about_option_nav
        locator.click()

    def click_log_out_option(self) -> None:
        """Clicks on "Log out" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = header_locators.log_out_option_nav
        locator.click()

    def click_reset_app_option(self) -> None:
        """Clicks on "Reset App State" in navigation.
        Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = header_locators.about_option_nav
        locator.click()

    def click_cart_icon(self) -> None:
        """Clicks on the cart icon
        """
        locator = header_locators.cart_icon
        locator.click()
