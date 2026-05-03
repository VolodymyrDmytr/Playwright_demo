import pytest
import allure

from config.constants import const
from config.parameters import param


@pytest.mark.ui
@pytest.mark.ui_product_page
@pytest.mark.parametrize(
    'product_data',
    [param.products[0], param.products[1], param.products[2],
     param.products[3], param.products[4], param.products[5],
     ],
)
def test_product_data(product, product_data, open_catalog_page):
    allure.dynamic.title(f"Check {product_data['title']}'s data")

    product.click_on_product(product_data['title'])

    product.check_product_title(product_data['title'])
    product.check_product_description(product_data['description'])
    product.check_product_price(product_data['price'])
    product.check_url(const.product_url(product_data['id']))


@pytest.mark.ui
@pytest.mark.ui_product_page
def test_back_to_catalog(product, open_catalog_page):
    allure.dynamic.title('Click Back to products button')

    product_data = param.get_random_product()

    product.click_on_product(product_data['title'])
    product.check_url(const.product_url(product_data['id']))

    product.click_back_to_products_button()
    product.check_url(const.catalog_url)


@pytest.mark.ui
@pytest.mark.ui_product_page
def test_add_to_cart(product, header, cart, open_catalog_page):
    allure.dynamic.title('Click Add to cart and Remove button')

    product_data = param.get_random_product()

    product.click_on_product(product_data['title'])
    product.check_url(const.product_url(product_data['id']))

    product.click_add_to_card_button()

    header.check_products_amount_in_the_cart(1)
    header.click_cart_icon()

    cart.check_cart_card(
        0,
        1,
        product_data['title'],
        product_data['description'],
        product_data['price'],
    )
    cart.sys_back()

    product.click_remove_button()
    header.check_products_amount_in_the_cart_is_not_visible()
