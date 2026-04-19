import pytest
import logging

from config.constants import const
from config.parameters import param

logger = logging.getLogger('Test Catalog Page')


# test_sorting test also close this check. So this test can be removed
@pytest.mark.ui
@pytest.mark.ui_catalog_page
def test_product_cards_data(catalog, open_catalog_page):
    for i in range(6):
        catalog.check_product_card(
            i,
            param.products[i]['title'],
            param.products[i]['description'],
            param.products[i]['price'],
        )


@pytest.mark.ui
@pytest.mark.ui_catalog_page
def test_adding_products_in_the_cart(catalog, header, open_catalog_page):
    for i in range(6):
        catalog.click_card_button(i)

    header.check_products_amount_in_the_cart(6)

    catalog.click_card_button(5)
    header.check_products_amount_in_the_cart(5)


@pytest.mark.ui
@pytest.mark.ui_catalog_page
@pytest.mark.parametrize(
    'product',
    [param.products[0], param.products[1], param.products[2],
     param.products[3], param.products[4], param.products[5],
     ],
)
def test_go_to_the_product_pages(catalog, product, open_catalog_page):
    catalog.click_on_product(product['title'])
    catalog.check_url(const.product_url(product['id']))


@pytest.mark.ui
@pytest.mark.ui_catalog_page
@pytest.mark.parametrize(
    'sort_type',
    [const.sort_type_a_z, const.sort_type_z_a, const.sort_type_high_price,
     const.sort_type_low_price,
     ],
)
def test_sorting(catalog, sort_type, open_catalog_page):
    logger.debug('Sort Type: %s', sort_type)
    catalog.choose_sort(sort_type)
    product_data = param.sort_products_dict(param.products, sort_type)

    for i in range(6):
        catalog.check_product_card(
            i,
            product_data[i]['title'],
            product_data[i]['description'],
            product_data[i]['price'],
        )
