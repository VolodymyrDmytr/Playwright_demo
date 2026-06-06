from pages.base_page import BasePage
from config.locators import OverviewLocators

from playwright.async_api import expect, Page
import allure
import logging

logger = logging.getLogger(__name__)


class OverviewPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = OverviewLocators(self.page)

    @allure.step("""Expected card {number} data:
                 Product amount: {amount}
                 Title: {title}
                 Description: {description}
                 Price: {price}""")
    async def check_product_card(
            self,
            number: int,
            amount: int,
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
        locator = self.locators.card.nth(number)

        amount_locator = self.locators.card_amount(locator)
        title_locator = self.locators.card_title(locator)
        description_locator = self.locators.card_description(locator)
        price_locator = self.locators.card_price(locator)

        await expect(amount_locator).to_have_text(str(amount))
        await expect(title_locator).to_have_text(title)
        await expect(description_locator).to_have_text(description)
        await expect(price_locator).to_have_text(price)

    @allure.step('Check all prices')
    async def check_prices(self) -> bool:
        """Check`s are item total, taxes and total as expected

        Returns:
            bool: True, if actual match expected
        """
        # Getting actual prices
        tax_locator = self.locators.tax
        taxes = tax_locator.text_content().replace('Tax: $', '')
        taxes = float(taxes)

        item_total_locator = self.locators.items_total
        item_total = item_total_locator.text_content().replace(
            'Item total: $', '')
        item_total = float(item_total)

        total_price_locator = self.locators.total_price
        total_price = total_price_locator.text_content().replace(
            'Total: $', '')
        total_price = float(total_price)

        # Calculating actual price
        expected_item_price = 0
        cards_locators = self.locators.card
        for i in range(cards_locators.count()):
            locator = cards_locators.nth(i)
            item_price = self.locators.card_price(locator).text_content(
            ).replace(
                '$', '')
            item_price = float(item_price)
            logger.debug('%s item price: %s', i, item_price)
            expected_item_price += item_price
            logger.debug('Current total price (%s): %s',
                         i, expected_item_price)

        # Calculating taxes
        expected_taxes = expected_item_price * 0.08

        # Calculating total sum
        expected_total_sum = expected_item_price + expected_taxes

        # Checking results
        logger.debug('Taxes: actual = %s, expected = %s',
                     taxes, expected_taxes)
        logger.debug('Total price: actual = %s, expected = %s',
                     total_price, expected_total_sum)
        logger.debug('Item total: actual = %s, expected = %s',
                     item_total, expected_item_price)

        assert taxes == round(expected_taxes, 2)
        assert item_total == round(expected_item_price, 2)
        assert total_price == round(expected_total_sum, 2)

    @allure.step('Click Cancel button')
    async def click_cancel_button(self) -> None:
        """Click`s "Cancel" button on Overview page
        """
        locator = self.locators.cancel_button
        await locator.click()

    @allure.step('Click Finish button')
    async def click_finish_button(self) -> None:
        """Click`s "Finish" button on Overview page
        """
        locator = self.locators.finish_button
        await locator.click()

    @allure.step('Check is shipping method is {data}')
    async def check_shipping_method(
            self,
            data: str,
    ) -> bool:
        """Check`s shipping method on Overview page

        Args:
            data (str): expected method

        Returns:
            bool: True, if shipping method matches expected result
        """
        locator = self.locators.delivery_method
        await expect(locator).to_have_text(data)
