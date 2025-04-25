from selenium.webdriver.common.by import By
from WebUIAutoshop.settings import ENV


class Home:
    def __init__(self, browser):
        self.driver = browser
        # self.driver.get_url(ENV.url)
        self.login_btn = (By.XPATH, "//a[@id='login']")
        self.login_msg = (By.XPATH, "//*[@id='top1']/p/a")
        self.user_center = (By.XPATH, "//img[@src='img/grzx.png']")
        self.first_goods = (By.XPATH, "(//span[@class='abr'])[1]")
        self.search = (By.XPATH, '//*[@id="top1"]/form/input[1]')
        self.search_btn = (By.XPATH, "//input[@type='submit']")
        self.search_father = (By.XPATH, "/html/body/div[3]/div/div")
        self.search_son = (By.XPATH, "/html/body/div[3]/div/div/a/dl/dd[1]")
        self.goods_name = (By.XPATH, "//dd[contains(text()]")
        self.search_result = (By.XPATH, "/html/body/div[3]/div/div/a/dl/dd[1]")

    # 点击登录按钮
    def click_login_btn(self):
        self.driver.click(self.login_btn)

    # 点击个人中心按钮
    def click_user_center(self):
        self.driver.click(self.user_center)

    # 点击第一个商品
    def click_first_goods(self):
        self.driver.click(self.first_goods)

    # 滚动到第一个商品可见
    def scroll_first_goods(self):
        self.driver.scroll_ele(self.first_goods)

    # 返回登录信息
    def find_login_msg(self):
        return self.driver.get_text(self.login_msg)

    # 在搜索框输入
    def sendkey_search(self, search):
        self.driver.send_keys(self.search, search)

    # 点击搜索按钮
    def click_search(self):
        self.driver.click(self.search_btn)

    # 返回搜索结果的所有商品名
    def find_search_result(self):
        name = []
        # x = 0
        # quantity_father = self.driver.find_elements(self.search_father)
        # quantity_son = self.driver.find_elements(self.search_son)
        # for i in range(len(quantity_father)-1):
        #     for j in range(4):
        #         x += 1
        #         if x > len(quantity_son):
        #             break
        #         else:
        #             goods_name = (By.XPATH, f"/html/body/div[3]/div/div[{i+1}]/a[{j+1}]/dl/dd[1]")
        #             text = self.driver.get_text(goods_name)
        #             name.append(text)
        quantity_father = self.driver.find_elements(self.search_father)
        for i, father in enumerate(quantity_father):
            quantity_son = father.find_elements(*self.search_son)
            for j, son in enumerate(quantity_son):
                name.append(son.text)
        return name

    def find_nofound_search(self):
        text = None
        return text

    # 滚动到搜索结果可见
    def scroll_search_result(self):
        self.driver.scroll(self.search_result)
