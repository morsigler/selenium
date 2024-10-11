from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class HomePage:
    mainUrl = "https://weathershopper.pythonanywhere.com/"

    def __init__(self, driver: WebDriver):
        self.driver = driver


    #### LOCATORS #####
    current_temperature = (By.ID, "temperature")
    buy_product_btn = (By.XPATH, "//button[contains(text(),'Buy PRODUCT_GROUP')]")


    def get_current_temperature(self):
        return self.driver.find_element(self.current_temperature[0],self.current_temperature[1])

    def get_buy_product_btn(self,product_group_name):
        self.newProductBtnLocator = (self.buy_product_btn[0],self.buy_product_btn[1].replace("PRODUCT_GROUP",product_group_name))
        return self.driver.find_element(self.newProductBtnLocator[0],self.newProductBtnLocator[1])

    #### METHODS ######
    def navigateToHomePage(self):
        self.driver.get(self.mainUrl)

    def should_buy_moisturizers_or_sunscreen(self):
        temp = [int(i) for i in self.get_current_temperature().text.split() if i.isdigit()][0]
        if temp < 19:
            print("Going to buy moisturizers")
            self.get_buy_product_btn("moisturizers").click()
            return "moisturizers"
        elif temp > 36:
            print("Going to buy sunscreens")
            self.get_buy_product_btn("sunscreens").click()
            return "sunscreens"
        else:
            print("you don't need to buy anything")

