from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self):
        self.page = Page()

    # Identificators

    @property
    def burger_menu_button(self) -> Locator:
        """Burger menu button in Header

        Returns:
            it`s locator
        """
        return self.page.get_by_alt_text('Open Menu')

    @property
    def close_navigation(self) -> Locator:
        """Close button button in Navigation

        Returns:
            it`s locator
        """
        return self.page.get_by_alt_text('Close Menu')

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
        return self.page.get_by_text('Log out')

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

    # Actions

    def open_navigation_menu(self) -> None:
        """Clicks on burger menu icon to open navigation
        """
        locator = self.burger_menu_button
        locator.click()

    def close_navigation_menu(self) -> None:
        """Clicks on "X" in navigation to close it. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.close_navigation
        locator.click()

    def click_all_items_option(self) -> None:
        """Clicks on "All items" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.all_items_option_nav
        locator.click()

    def click_about_option(self) -> None:
        """Clicks on "About" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.about_option_nav
        locator.click()

    def click_log_out_option(self) -> None:
        """Clicks on "Log out" in navigation. Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.log_out_option_nav
        locator.click()

    def click_reset_app_option(self) -> None:
        """Clicks on "Reset App State" in navigation.
        Navigation should be opened
        Use open_navigation_menu method to open it
        """
        locator = self.about_option_nav
        locator.click()

    def click_cart_icon(self) -> None:
        """Clicks on the cart icon
        """
        locator = self.cart_icon
        locator.click()
