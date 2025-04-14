from selenium.webdriver.common.by import By

from WebUIAutoshop.common.log import log


class GoodsDetails:
    def __init__(self, browser):
        self.driver = browser
        self.quantity_up = (By.XPATH, "//img[@class='fl add']")
        self.quantity_down = (By.XPATH, "//img[@class='fl sub']")
        self.buy_now = (By.XPATH, "//p[@class='buy fl']")
        self.add_car = (By.XPATH, "//p[@class='cart fr']")
        self.inventory = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div[2]/p[2]/span")

    # 点击数量+
    def click_quantity_up(self):
        self.driver.click(self.quantity_up)

    # 点击数量-
    def click_quantity_down(self):
        self.driver.click(self.quantity_down)

    # 点击立即购买
    def click_buy_now(self):
        self.driver.click(self.buy_now)
        log.info("点击立即购买")

    # 点击加入购物车
    def click_add_car(self):
        self.driver.click(self.add_car)
