import re

from selenium.webdriver.common.by import By

from WebUIAutoshop.common.log import log


class Order:
    def __init__(self, browser):
        self.driver = browser
        self.address = (By.XPATH, "//div[@class='addCon']//p[1]")
        self.now_pay = (By.XPATH, "//a[contains(text(),'去支付')]")
        self.total = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/p/span[2]")
        self.goods_father = (By.CSS_SELECTOR, "body > div.order.cart.mt > div.orderCon.wrapper.clearfix > div.orderR.fr > div.msg")
        self.goods_son = (By.CSS_SELECTOR, "body > div.order.cart.mt > div.orderCon.wrapper.clearfix > div.orderR.fr > div.msg > ul")
        self.order_id = (By.XPATH, "//li[contains(text(),'订单号:')]")
        # self.goods_son = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/ul[*]')

    # 点击去支付
    def click_now_pay(self):
        self.driver.click(self.now_pay)

    # 返回收货地址
    def find_address(self):
        address = self.driver.get_text(self.address)
        return address

    # 返回合计金额
    def find_total(self):
        total = re.findall(r'\d+', self.driver.get_text(self.total))
        return int(total[0])

    # 返回订单里的商品数量
    def find_quantity_all(self):
        # a = self.driver.find_element_CSS(self.goods_father)
        quantity = self.driver.find_elements(self.goods_son)
        return len(quantity)

    # 返回第一个订单id
    def find_order_id(self):
        order_id = self.driver.get_text(self.order_id)
<<<<<<< HEAD
        if order_id is None:
            return None
=======
>>>>>>> b0c550d611f6f8e2440119172c9ea705be8e13e0
        return order_id.split(":")[1]

    # 返回订单里的商品信息
    def find_order_details(self):
        array = []
        quantity_all = self.find_quantity_all()
        if quantity_all >= 1:
            for i in range(quantity_all):
                goods_name = (By.XPATH, f"/html/body/div[2]/div[2]/div[2]/div[1]/ul[{i+1}]/li[2]/p[1]")
                goods_quantity = (By.XPATH, f"/html/body/div[2]/div[2]/div[2]/div[1]/ul[{i+1}]/li[2]/p[3]")
                goods_subtotal = (By.XPATH, f"/html/body/div[2]/div[2]/div[2]/div[1]/ul[{i+1}]/li[3]")
                name = str(self.driver.get_text(goods_name))
                quantity = re.findall(r'\d+', self.driver.get_text(goods_quantity))
                subtotal = re.findall(r'\d+', self.driver.get_text(goods_subtotal))
                array.extend((name, int(quantity[0]), int(subtotal[0])))
        else:
            log.error("商品数量小于1！")
        return array
