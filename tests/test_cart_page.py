import pytest
from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_empty_cart(cart, header, open_catalog_page):
    header.click_cart_icon()
    cart.check_no_cards()


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_continue_shopping_button(cart, header, open_catalog_page):
    header.click_cart_icon()

    cart.click_continue_shopping_button()
    cart.check_url(const.catalog_url)


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_product_data(cart, open_cart_page_with_products):
    products = param.sort_products_dict(param.products, const.sort_type_a_z)
    for i in range(len(param.products)-1):
        cart.check_cart_card(
            i,
            1,
            products[i]['title'],
            products[i]['description'],
            products[i]['price'],
        )


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_checkout_button(cart, open_cart_page_with_products):
    cart.click_checkout_button()
    cart.check_url(const.checkout_1st_step_url)


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_removing_products(cart, open_cart_page_with_products):
    cart.click_remove_button(-1)
    for i in range(len(param.products)-2):
        cart.check_cart_card(
            i,
            1,
            param.products[i]['title'],
            param.products[i]['description'],
            param.products[i]['price'],
        )


@pytest.mark.ui
@pytest.mark.ui_cart_page
def test_open_product(cart, header, open_cart_page_with_products):
    for i in range(len(param.products)):
        cart.click_on_product(param.products[i]['title'])
        cart.check_url(const.product_url(param.products[i]['id']))
        header.click_cart_icon()
