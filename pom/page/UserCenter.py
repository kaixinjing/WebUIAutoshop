import re

from selenium.webdriver.common.by import By

from WebUIAutoshop.common.log import log


class UserCenter:
    def __init__(self, browser):
        self.driver = browser
        # 退出登录
        self.user_quit = (By.XPATH, "//a[contains(text(),'退出登录')]")
        # 用户名称
        self.user_name = (By.XPATH, "//p[@class='fl']//span[contains(text(),'')][1]")
        # 修改个人信息
        self.update_user = (By.XPATH, "//a[contains(text(),'修改个人信息>')]")
        self.edit = (By.XPATH, "(//a[contains(text(),'编辑')])")
        self.name = (By.XPATH, "//input[@name='name']")
        self.phone = (By.XPATH, "//input[@name='phone']")
        self.email = (By.XPATH, "//input[@name='email']")
        self.address = (By.XPATH, "//input[@name='address']")
        self.save = (By.XPATH, "//input[@value='保存']")
        # 我的订单
        self.my_order = (By.XPATH, "/html/body/div[3]/div/div[1]/div/ul/li[3]/a")
        # 我的购物车
        self.my_car = (By.XPATH, "//a[contains(text(),'我的购物车')]")
        # 订单金额
        self.order_total = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/p/span")
        # 订单状态
        self.order_state = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/p")
        self.order_id = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/ul/li[3]")
        # 下单人
        self.order_user = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/ul/li[2]")
        # 订单操作
        self.order_operate = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[3]/p/a")

        self.goods_father = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]")
        self.goods_son = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div")
        # 第一个商品名
        self.goods_name = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[2]/p/a[1]")
        self.goods_quantity_subtotal = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[2]/p/a[2]")

    # 点击退出登录
    def click_user_quit(self):
        self.driver.click(self.user_quit)

    # 点击订单的操作
    def click_order_operate(self):
        self.driver.click(self.order_operate)

    # 点击修改个人信息
    def click_update_user(self):
        self.driver.click(self.update_user)

    # 点击修改个人信息_编辑
    def click_edit(self):
        self.driver.click(self.edit)

    # 点击我的订单
    def click_my_order(self):
        self.driver.click(self.my_order)

    # 点击我的购物车
    def click_my_car(self):
        self.driver.click(self.my_car)

    # 返回第一个订单id
    def find_order_id(self):
        order_id = self.driver.get_text(self.order_id)
        return order_id.split(":")[1]

    # 返回订单状态
    def find_order_state(self):
        state = self.driver.get_text(self.order_state)
        return state

    # 返回下单人
    def find_order_user(self):
        user = self.driver.get_text(self.order_user)
        return user

    # 返回订单总金额
    def find_order_total(self):
        total = self.driver.get_text(self.order_total)
        return int(float(total))

    # 返回商品名称
    # def find_good_name(self):
    #     self.driver.find_elements(self.goods_name)
    #     name = self.driver.get_text(self.goods_name)

    # 返回所有商品数量
    def find_quantity_all(self):
        # a = self.driver.find_element(self.goods_father)
        quantity = self.driver.find_elements(self.goods_son)
        return len(quantity)-2

    # 返回订单详情信息(商品名称,商品数量,商品单价)
    def find_order_details(self):
        array = []
        quantity_all = self.find_quantity_all()
        if quantity_all >= 1:
            for i in range(quantity_all):
                goods_name = (By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[{i+2}]/p/a[1]")
                goods_quantity_subtotal = (By.XPATH, f"/html/body/div[3]/div/div[2]/div[3]/div[{i+2}]/p/a[2]")
                name = str(self.driver.get_text(goods_name))
                quantity_subtotal = re.findall(r'\d+', self.driver.get_text(goods_quantity_subtotal))
                array.extend((name, int(quantity_subtotal[0]), int(quantity_subtotal[1])))
        else:
            log.error("商品数量小于1！")
        return array

    # 返回用户名称
    def find_user_name(self):
        return self.driver.get_text(self.user_name)

    # 修改个人信息
    def edit_user(self, name, phone, email, address):
        self.driver.send_keys(self.name, name)
        self.driver.send_keys(self.phone, phone)
        self.driver.send_keys(self.email, email)
        self.driver.send_keys(self.address, address)
        self.driver.click(self.save)
