import pytest
import allure

from config.constants import const


@pytest.mark.ui
@pytest.mark.ui_done_page
def test_page_text(done, open_done_page):
    allure.dynamic.title('Check text and alt for image on page')

    done.check_title(const.done_title)
    done.check_text(const.done_text)
    done.check_image(const.done_alt_image)


@pytest.mark.ui
@pytest.mark.ui_done_page
def test_back_button(done, open_done_page):
    allure.dynamic.title('Click Back to home button')

    done.click_back_to_home_button()
    done.check_url(const.catalog_url)
