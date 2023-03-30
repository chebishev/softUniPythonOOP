from horse_racings.project import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Shop", 2000)

    def test_init_name(self):
        self.assertEqual(self.shopping_cart.shop_name, "Shop")

    def test_name_not_upper(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "shop"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_not_alpha(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "5hop"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_not_upper_not_alpha(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "sh0p"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_name_upper_not_alpha(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Sh1p"
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart(self):
        product_name = "Glasses"
        product_price = 99.99
        self.assertEqual(self.shopping_cart.add_to_cart(product_name, product_price),
                         f"{product_name} product was successfully added to the cart!")
        self.assertEqual(self.shopping_cart.products, {product_name: product_price})

    def test_price_over_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Glasses", 100.00)
        self.assertEqual(str(ve.exception), "Product Glasses cost too much!")

    def test_remove_from_cart(self):
        self.shopping_cart.add_to_cart("Glasses", 99.99)
        self.shopping_cart.add_to_cart("Sun Creme", 99.99)
        self.assertEqual(self.shopping_cart.remove_from_cart("Glasses"),
                         f"Product Glasses was successfully removed from the cart!")
        self.assertEqual(self.shopping_cart.products, {"Sun Creme": 99.99})

    def test_invalid_remove_from_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Glasses")
        self.assertEqual(str(ve.exception), "No product with name Glasses in the cart!")

    def test_add_method(self):
        self.shopping_cart.products = {
            "Sun Creme": 99.99
        }
        new_shop = ShoppingCart("Posh", 200)
        new_shop.products = {"Glasses": 99.99}
        new_shopping_cart = self.shopping_cart.__add__(new_shop)
        self.assertEqual(new_shopping_cart.shop_name, "ShopPosh")
        self.assertEqual(new_shopping_cart.budget, 2200)
        self.assertEqual(new_shopping_cart.products, {"Sun Creme": 99.99, "Glasses": 99.99})

    def test_buy_products(self):
        self.shopping_cart.products = {
            "Sun Creme": 99.99,
            "Glasses": 99.99
        }
        total_sum = 199.98
        self.assertEqual(self.shopping_cart.buy_products(),
                         f'Products were successfully bought! Total cost: {total_sum:.2f}lv.')

    def test_buy_products_not_enough_budget(self):
        self.shopping_cart.budget = 197.98
        self.shopping_cart.products = {
            "Sun Creme": 99.99,
            "Glasses": 99.99
        }
        total_sum = 199.98
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual(str(ve.exception), f"Not enough money to buy the products! Over budget with 2.00lv!")


if __name__ == "__main__":
    main()
