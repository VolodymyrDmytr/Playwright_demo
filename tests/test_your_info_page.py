import pytest

from config.constants import const
from config.faker_settings import faker


@pytest.mark.ui
@pytest.mark.ui_your_info_page
def test_filling_field(your_info, open_your_info_page):
    your_info.fill_first_name_field(faker.first_name())
    your_info.fill_last_name_field(faker.last_name())
    your_info.fill_postal_code_field(faker.postcode())
    your_info.press_continue_button()
    your_info.check_url(const.checkout_2nd_step_url)


@pytest.mark.ui
@pytest.mark.ui_your_info_page
def test_cancel(your_info, open_your_info_page):
    your_info.press_cancel_button()
    your_info.check_url(const.cart_url)


@pytest.mark.ui
@pytest.mark.ui_your_info_page
def test_error_in_fields(your_info, open_your_info_page):
    your_info.press_continue_button()
    your_info.check_url(const.checkout_1st_step_url)

    your_info.check_error_text(const.missing_first_name)
    your_info.check_error_icons_in_fields()

    your_info.fill_first_name_field(faker.first_name())
    your_info.press_continue_button()

    your_info.check_error_text(const.missing_last_name)
    your_info.check_error_icons_in_fields()

    your_info.fill_last_name_field(faker.last_name())
    your_info.press_continue_button()

    your_info.check_error_text(const.missing_postal_code)
    your_info.check_error_icons_in_fields()

    your_info.close_error_block()

    your_info.check_is_error_block_absent()
    your_info.check_missing_error_icons_in_fields()
