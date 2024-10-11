from page_objects.HomePage import HomePage
from page_objects.ProductsPage import ProductsPage


class Test_main_flow():

    def test_main_flow(self,driver):
        self.moist_or_sunscreen = ""
        self.home_page = HomePage(driver)
        self.product_page = ProductsPage(driver)

        self.home_page.navigateToHomePage()
        self.moist_or_sunscreen = self.home_page.should_buy_moisturizers_or_sunscreen()
        if self.moist_or_sunscreen == "moisturizers":
            self.product_page.add_products_to_cart("Aloe")
            self.product_page.add_products_to_cart("Almond")
        else:
            self.product_page.add_products_to_cart("SPF-30")
            self.product_page.add_products_to_cart("SPF-50")

