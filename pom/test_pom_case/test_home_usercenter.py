import os
import subprocess
import time

import allure
import pytest
from time import sleep

from selenium.webdriver.common.by import By

from WebUIAutoshop.common.log import log
from WebUIAutoshop.pom.base.Event import Event
from WebUIAutoshop.pom.page.GoodsDetails import GoodsDetails
from WebUIAutoshop.pom.page.Home import Home
from WebUIAutoshop.pom.page.Order import Order
from WebUIAutoshop.pom.page.ShopCar import ShopCar
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.settings import ENV


class TestHomeUserCenter:
    def test_shop_016_skip_login(self, browser):
        driver = browser
        home = Home(driver)
        home.sendkey_search("花")
        home.click_search()
        sleep(0.2)
        home.scroll_search_result()
        text = home.find_search_result()
        log.info(f"搜索：花, in 结果：{text}")
        assert "花" in text[0]

    def test_shop_017_skip_login(self, browser):
        driver = browser
        home = Home(driver)
        home.sendkey_search("哈哈")
        home.click_search()
        sleep(0.2)
        text = home.find_nofound_search()
        log.info(f"搜索：哈哈, in 结果：{text}")
        assert text is None

    def test_shop_018_skip_login(self, browser):
        driver = browser
        home = Home(driver)
        home.click_search()
        sleep(0.2)
        text = home.find_search_result()
        log.info(f"空搜索,数量：{len(text)},结果：{text}")
        assert len(text) > 0

    def test_shop_019(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_buy_now()
        driver.get_url(ENV.UserCenter)
        log.info("跳转到个人中心")
        usercenter = UserCenter(driver)
        usercenter.click_my_order()
        log.info("进入订单页")
        state1 = usercenter.find_order_state()
        log.info(f"当前订单状态为：{state1}")
        if state1 == "待支付":
            usercenter.click_order_operate()
            state2 = usercenter.find_order_state()
            log.info(f"操作后订单状态为：{state2}")
            assert state2 == "已支付"
        else:
            log.info("当前订单状态异常")

    def test_shop_020(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_buy_now()
        order = Order(driver)
        order.click_now_pay()
        order_id1 = order.find_order_id()
        usercenter = UserCenter(driver)
        usercenter.click_order_operate()
        log.info("点击：删除订单")
        order_id2 = order.find_order_id()
        assert order_id1 != order_id2

    def test_shop_021(self, browser):
        driver = browser
        driver.get_url(ENV.UserCenter)
        usercenter = UserCenter(driver)
        usercenter.click_my_car()
        shopcar = ShopCar(driver)
        shopcar_name = shopcar.find_shopcar_name()
        log.info(f"shopcar名称为：{shopcar_name}")
        assert shopcar_name == '购物车'

    @allure.feature("个人中心")
    @allure.step("修改个人信息")
    @pytest.mark.parametrize("name, phone, email, address", [('admin', '123456', '123@qq.com', '北京')])
    def test_shop_022(self, name, phone, email, address, browser):
        driver = browser
        driver.get_url(ENV.UserCenter)
        usercenter = UserCenter(driver)
        usercenter.click_update_user()
        usercenter.click_edit()
        usercenter.edit_user(name, phone, email, address)
        user_name = usercenter.find_user_name()
        log.info(f"修改用户成功，名称为：{user_name}")
        assert user_name == name

    def test_shop_023_skip_login(self, browser):
        driver = browser
        driver.get_url(ENV.url)
<<<<<<< HEAD
        log.info("本用例故意制造错误，测试将错误截图保存到allure报告中")
        driver.find_element(By.XPATH, "//img[@src='img/laaaogo.png']")


if __name__ == '__main__':
    pytest.main(['-vs', 'test_home_usercenter.py::TestHomeUserCenter::test_shop_020'])
    #pytest.main(['-vs', 'test_home_usercenter.py::TestHomeUserCenter::test_shop_023_skip_login', '--clean-alluredir',
    #             '--alluredir=../../allure_result'])
    #os.system(r"allure generate ../../allure_result -o ../../allure_page -c")
    #subprocess.Popen(r"allure open ../../allure_page", shell=True)
=======
        driver.find_element(By.XPATH, "//img[@src='img/laaaogo.png']")



if __name__ == '__main__':
    # pytest.main(['-vs', 'test_home_usercenter.py::TestHomeUserCenter::test_shop_023'])
    pytest.main(['-vs', 'test_home_usercenter.py::TestHomeUserCenter::test_shop_023_skip_login', '--clean-alluredir',
                 '--alluredir=../../allure_result'])
    os.system(r"allure generate ../../allure_result -o ../../allure_page -c")
    subprocess.Popen(r"allure open ../../allure_page", shell=True)
>>>>>>> b0c550d611f6f8e2440119172c9ea705be8e13e0
