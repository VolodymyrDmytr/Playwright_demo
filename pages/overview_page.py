from pages.base_page import BasePage

from playwright.sync_api import expect
from config.locators import overview_locators


class OverviewPage(BasePage):

    def __init__(self):
        super().__init__()

    def check_cart_card(
            self,
            number: int,
            title: str,
            description: str,
            price: str,
    ) -> bool:
        """Check data in the card on Overview page

        Args:
            number (int): card number
            title (str): product`s title
            description (str): product`s description
            price (str): product`s price

        Returns:
            bool: True, if data matches expectations
        """
        number -= 1
        locator = overview_locators.card.nth(number)

        title_locator = overview_locators.card_title(locator)
        description_locator = overview_locators.card_description(locator)
        price_locator = overview_locators.card_price(locator)

        expect(title_locator).to_have_text(title)
        expect(description_locator).to_have_text(description)
        expect(price_locator).to_have_text(price)

    def check_prices(self) -> bool:
        """Check`s are item total, taxes and total as expected

        Returns:
            bool: True, if actual match expected
        """
        # Getting actual prices
        tax_locator = overview_locators.tax
        taxes = tax_locator.text_content().replace('Tax $', '')
        taxes = int(taxes)

        item_total_locator = overview_locators.items_total
        item_total = item_total_locator.text_content().replace(
            'Item total: $', '')
        item_total = int(item_total)

        total_price_locator = overview_locators.total_price
        total_price = total_price_locator.text_content().replace(
            'Total: $', '')
        total_price = int(total_price)

        # Calculating actual price
        expected_item_price = 0
        cards_locators = overview_locators.card
        for i in range(len(cards_locators) - 1):
            locator = cards_locators.nth(i)
            item_price = overview_locators.card_price(locator).text_content(
            ).replace(
                '$', '')
            item_price = int(item_price)
            expected_item_price += item_price

        # Calculating taxes
        expected_taxes = expected_item_price * 0.08

        # Calculating total sum
        expected_total_sum = expected_item_price + expected_taxes

        # Checking results
        assert taxes == expected_taxes
        assert item_total == expected_item_price
        assert total_price == expected_total_sum

    def click_cancel_button(self) -> None:
        """Click`s "Cancel" button on Overview page
        """
        locator = overview_locators.cancel_button
        locator.click()

    def click_finish_button(self) -> None:
        """Click`s "Finish" button on Overview page
        """
        locator = overview_locators.finish_button
        locator.click()

    def check_shipping_method(
            self,
            data: str,
    ) -> bool:
        """Check`s shipping method on Overview page

        Args:
            data (str): expected method

        Returns:
            bool: True, if shipping method matches expected result
        """
        locator = overview_locators.delivery_method
        expect(locator).to_have_text(data)
