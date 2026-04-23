class Constants:
    page_title = 'Swag Labs'

    # URL`s
    login_url = 'https://www.saucedemo.com/'
    catalog_url = login_url + 'inventory.html'
    cart_url = login_url + 'cart.html'
    about_url = 'https://saucelabs.com/'
    checkout_1st_step_url = login_url + 'checkout-step-one.html'
    checkout_2nd_step_url = login_url + 'checkout-step-two.html'
    done_url = login_url + 'checkout-complete.html'

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

    # Errors on Login page
    incorrect_login_data = ('Epic sadface: Username and password do not match'
                            + ' any user in this service')
    missing_username = 'Epic sadface: Username is required'
    missing_password = 'Epic sadface: Password is required'
    blocked_user = 'Epic sadface: Sorry, this user has been locked out.'

    # Errors on Overview page
    missing_first_name = 'Error: First Name is required'
    missing_last_name = 'Error: Last Name is required'
    missing_postal_code = 'Error: Postal Code is required'

    # Done page text
    done_title = 'Thank you for your order!'
    done_text = ('Your order has been dispatched, and will arrive just as '
                 + 'fast as the pony can get there!')
    done_alt_image = 'Pony Express'


const = Constants()
