import re
from selenium.webdriver.common.by import By
from WebUIAutoshop.common.log import log


class ShopCar:
    def __init__(self, browser):
        self.driver = browser
        # 勾选所有商品
        self.check_all = (By.XPATH, "//div[@class='tr clearfix']//label[@class='fl']//span")
        # 商品名称
        self.goods_name = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/a/dl/dd/p[1]")
        # 页面商品的父元素(用来判断有几个)
        self.goods_father = (By.XPATH, "/html/body/div[2]/div[2]")
        self.goods_son = (By.CLASS_NAME, "th")
        # 继续购物
        self.continue_shop = (By.XPATH, "//a[@class='fr']")
        # 左上角购物车
        self.shopcar_name = (By.XPATH, "//span[contains(text(),'购物车')]")
        # 单价
        self.unit_price = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[2]/div[2]")
        # 数量
        self.quantity = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[2]/div[3]/p[1]/span[1]")
        self.quantity_up = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[2]/div[3]/p[1]/img[2]")
        self.quantity_down = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[2]/div[3]/p[1]/img[1]")
        self.quantity_all = (By.XPATH, "//small[@id='sl']")
        # 小计
        self.subtotal = (By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[2]/div[4]")
        self.delete = (By.XPATH, "(//a[contains(text(),'删除')])[1]")
        # 金额合计
        self.total = (By.XPATH, "//small[@id='all']")
        # 结算按钮
        self.buy = (By.XPATH, "//a[contains(text(),'结算')]")

    # 点击选择所有商品
    def click_check_all(self):
        self.driver.click(self.check_all)
        log.info("点击选择所有商品")

    # 点击第一个商品的数量+
    def click_quantity_up(self):
        self.driver.click(self.quantity_up)
        log.info("点击商品+")

    # 点击第一个商品的数量-
    def click_quantity_down(self):
        self.driver.click(self.quantity_down)
        log.info("点击商品-")

    # 点击第一个商品的删除
    def click_delete(self):
        self.driver.click(self.delete)
        log.info("点击商品删除")

    # 返回结算按钮是否可点击
    def find_buy(self):
        return self.driver.find_is_enabled(self.buy)

    # 点击结算按钮
    def click_buy(self):
        self.driver.click(self.buy)
        log.info("点击结算按钮")

    # 点击继续购物按钮
    def click_continue_shop(self):
        self.driver.click(self.continue_shop)
        log.info("点击继续购物")

    # 返回左上角购物车名称
    def find_shopcar_name(self):
        return self.driver.get_text(self.shopcar_name)

    # 返回第一个商品的小计金额
    def find_subtotal(self):
        subtotal = int(self.driver.get_text(self.subtotal))
        return subtotal

    # 返回第一个商品的数量
    def find_good_quantity(self):
        good_quantity = int(self.driver.get_text(self.quantity))
        return good_quantity

    # 返回页面上的总金额
    def find_total(self):
        total = re.findall(r'\d+', self.driver.get_text(self.total))
        return int(total[0])

    # 返回页面上的所有商品数量
    def find_quantity_all(self):
        quantity = self.driver.find_elements(self.goods_son)
        if quantity is None:
            return 0
        return len(quantity)

    # 计算并返回所有商品金额(用于断言)
    def sum_money(self):
        self.click_check_all()
        quantity_all = self.find_quantity_all()
        real_total = 0
        if quantity_all >= 1:
            for i in range(quantity_all):
                unit_price = (By.XPATH, f"/html[1]/body[1]/div[2]/div[2]/div[{i + 2}]/div[2]")
                quantity = (By.XPATH, f"/html[1]/body[1]/div[2]/div[2]/div[{i + 2}]/div[3]/p[1]/span[1]")
                # subtotal = (By.XPATH, f"/html[1]/body[1]/div[2]/div[2]/div[{i + 2}]/div[4]")
                unit_price1 = re.findall(r'\d+', self.driver.get_text(unit_price))
                quantity1 = int(self.driver.get_text(quantity))
                real_total = int(unit_price1[0]) * quantity1 + real_total
        else:
            log.error("商品数量小于1！")
        log.info(f"购物车总金额为：{real_total}")
        return real_total

    # 返回购物车里的所有商品信息
    def find_car_details(self):
        array = []
        quantity_all = self.find_quantity_all()
        if quantity_all >= 1:
            for i in range(quantity_all):
                goods_name = (By.XPATH, f"/html/body/div[2]/div[2]/div[{i + 2}]/div[1]/a/dl/dd/p[1]")
                goods_quantity = (By.XPATH, f"/html[1]/body[1]/div[2]/div[2]/div[{i + 2}]/div[3]/p[1]/span[1]")
                goods_subtotal = (By.XPATH, f"/html/body/div[2]/div[2]/div[{i + 2}]/div[4]")
                name = str(self.driver.get_text(goods_name))
                quantity = int(self.driver.get_text(goods_quantity))
                subtotal = re.findall(r'\d+', self.driver.get_text(goods_subtotal))
                array.extend((name, quantity, int(subtotal[0])))
        else:
            log.error("商品数量小于1！")
        return array
