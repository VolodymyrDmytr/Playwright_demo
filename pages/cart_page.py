from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.page = Page()
