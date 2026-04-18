import logging
import random

logger = logging.getLogger(__name__)


class Parameters:
    products = [
        {
            'id': 4,
            'title': 'Sauce Labs Backpack',
            'title_to_sort': 'Backpack',
            'description': (
                'carry.allTheThings() with the sleek, streamlined Sly Pack '
                + 'that melds uncompromising style with unequaled laptop and '
                + 'tablet protection.'),
            'price': '$29.99',
        },
        {
            'id': 0,
            'title': 'Sauce Labs Bike Light',
            'title_to_sort': 'Bike Light',
            'description': (
                "A red light isn't the desired state in testing but it sure "
                + 'helps when riding your bike at night. Water-resistant with'
                + ' 3 lighting modes, 1 AAA battery included.'),
            'price': '$9.99',
        },
        {
            'id': 1,
            'title': 'Sauce Labs Bolt T-Shirt',
            'title_to_sort': 'Bolt T-Shirt',
            'description': (
                'Get your testing superhero on with the Sauce Labs bolt '
                + 'T-shirt. From American Apparel, 100% '
                + 'ringspun combed cotton, heather gray with red bolt.'),
            'price': '$15.99',
        },
        {
            'id': 5,
            'title': 'Sauce Labs Fleece Jacket',
            'title_to_sort': 'Fleece Jacket',
            'description': (
                "It's not every day that you come across a "
                + 'midweight quarter-zip fleece jacket capable of '
                + 'handling everything from a relaxing day '
                + 'outdoors to a busy day at the office.'),
            'price': '$49.99',
        },
        {
            'id': 2,
            'title': 'Sauce Labs Onesie',
            'title_to_sort': 'Onesie',
            'description': (
                'Rib snap infant onesie for the junior automation '
                + 'engineer in development. Reinforced 3-snap '
                + 'bottom closure, two-needle hemmed sleeved and '
                + "bottom won't unravel."),
            'price': '$7.99',
        },
        {
            'id': 3,
            'title': 'Test.allTheThings() T-Shirt (Red)',
            'title_to_sort': 'T-shirt',
            'description': (
                'This classic Sauce Labs t-shirt is perfect to wear when '
                + 'cozying up to your keyboard to automate a few tests. '
                + 'Super-soft and comfy ringspun combed cotton.'),
            'price': '$15.99',
        },
    ]

    def sort_products_dict(
            self,
            data: list,
            sort_type: str,
    ) -> list:
        """Make sorting for dict. It is required because of existed sorting on
        catalog page. Also, to make forming test data easier

        Args:
            data (list): list of dicts to sort
            sort_type (str): sorting constants

        Returns:
            list: Sorted dict
        """
        if sort_type == 'az':
            data = sorted(data, key=lambda x: x['title_to_sort'].lower())
        elif sort_type == 'za':
            data = sorted(data, key=lambda x: x['title_to_sort'].lower(),
                          reverse=True)
        elif sort_type == 'lohi':
            data = sorted(data,
                          key=lambda x: float(x['price'].replace('$', '')))
        elif sort_type == 'hilo':
            data = sorted(data,
                          key=lambda x: float(x['price'].replace('$', '')),
                          reverse=True)
        logger.debug('Sorted products(%s): %s', sort_type, data)
        return data

    def get_random_product(self) -> dict:
        """Returns random product from available

        Returns:
            dict: Random product
        """
        length = len(self.products)
        return self.products[random.randint(0, length-1)]

    # name = (username, password)
    standart_user = ('standard_user', 'secret_sauce')
    locked_user = ('locked_out_user', 'secret_sauce')
    problem_user = ('problem_user', 'secret_sauce')
    glitch_user = ('performance_glitch_user', 'secret_sauce')
    error_user = ('error_user', 'secret_sauce')
    visual_user = ('visual_user', 'secret_sauce')


param = Parameters()
print(param.sort_products_dict(param.products, 'z_a'))
