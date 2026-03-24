class Constants:
    page_title = 'Swag Labs'

    # URL`s
    login_url = 'https://www.saucedemo.com/'
    catalog_url = login_url + 'inventory.html'
    cart_url = login_url + 'cart.html'

    def product_url(self, product_id: int) -> str:
        """Return product URL depending on it`s ID

        Args:
            product_id (int): existing product`s ID

        Returns:
            str: Product`s URL
        """
        return self.login_url + f'inventory-item.html?id={product_id}'

    # Sort on catalog page
    sort_type_a_z = 'az'
    sort_type_z_a = 'za'
    sort_type_low_price = 'lohi'
    sort_type_high_price = 'hilo'


const = Constants()
