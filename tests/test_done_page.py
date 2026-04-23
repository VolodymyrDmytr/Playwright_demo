import pytest

from config.constants import const


@pytest.mark.ui
@pytest.mark.ui_done_page
def test_page_text(done, open_done_page):
    done.check_title(const.done_title)
    done.check_text(const.done_text)
    done.check_image(const.done_alt_image)


@pytest.mark.ui
@pytest.mark.ui_done_page
def test_back_button(done, open_done_page):
    done.click_back_to_home_button()
    done.check_url(const.catalog_url)
