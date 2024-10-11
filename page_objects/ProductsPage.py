from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    #### LOCATORS #####
    product_by_condition = (By.XPATH, "//p[contains(text(),'CONDITION')]")
    add_btn = (By.XPATH, "//button[contains(text(),'Add')]")
    price = (By.XPATH, "//p[contains(text(),'Price: Rs. ')]")


    #returns list
    def get_products_by_text(self,condition):
        self.new_product_by_condition = (self.product_by_condition[0],self.product_by_condition[1].replace("CONDITION",condition))
        return self.driver.find_elements(self.new_product_by_condition[0],self.new_product_by_condition[1])

    #### METHODS ######
    def add_products_to_cart(self, product_condition):
        self.products_list = self.get_products_by_text(product_condition)
        if len(self.products_list) < 1:
            print("There are no item compatibale with "+product_condition)
        if len(self.products_list) == 1:
            self.products_list[0].find_element(self.add_btn[0], self.add_btn[1])
        else:
            self.firstProductPrice = self.products_list[0].find_element(self.price[0], self.price[1])
            self.lowest_price=  [int(i) for i in self.firstProductPrice.text.split() if i.isdigit()][0]
            for i in range(1, len(self.products_list)):
                self.product_price = self.products_list[i].find_element(self.price[0], self.price[1])
                if self.product_price < self.lowest_price:
                    self.lowest_price = self.product_price
        assert self.lowest_price == 0

