from pages.base_page import BasePage

from playwright.sync_api import expect, Locator


class OverviewPage(BasePage):

    def __init__(self):
        super().__init__()

    # Locators

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
        return self.page.locator('.checkout_button')

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

    # Actions
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
        locator = self.card.nth(number)

        title_locator = self.card_title(locator)
        description_locator = self.card_description(locator)
        price_locator = self.card_price(locator)

        expect(title_locator).to_have_text(title)
        expect(description_locator).to_have_text(description)
        expect(price_locator).to_have_text(price)

    def check_prices(self) -> bool:
        """Check`s are item total, taxes and total as expected

        Returns:
            bool: True, if actual match expected
        """
        # Getting actual prices
        tax_locator = self.tax
        taxes = tax_locator.text_content().replace('Tax $', '')
        taxes = int(taxes)

        item_total_locator = self.items_total
        item_total = item_total_locator.text_content().replace(
            'Item total: $', '')
        item_total = int(item_total)

        total_price_locator = self.total_price
        total_price = total_price_locator.text_content().replace(
            'Total: $', '')
        total_price = int(total_price)

        # Calculating actual price
        expected_item_price = 0
        cards_locators = self.card
        for i in range(len(cards_locators) - 1):
            locator = cards_locators.nth(i)
            item_price = self.card_price(locator).text_content().replace(
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
        locator = self.cancel_button
        locator.click()

    def click_finish_button(self) -> None:
        """Click`s "Finish" button on Overview page
        """
        locator = self.finish_button
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
        locator = self.delivery_method

        expect(locator).to_have_text(data)
