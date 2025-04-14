import os

import allure
import pytest
from time import sleep
from WebUIAutoshop.common.log import log
from WebUIAutoshop.pom.page.Order import Order
from WebUIAutoshop.pom.page.GoodsDetails import GoodsDetails
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.pom.page.Home import Home
from WebUIAutoshop.pom.page.ShopCar import ShopCar
from WebUIAutoshop.pom.base.Event import Event
from WebUIAutoshop.settings import ENV


class TestCarOrder:
    @allure.feature("购物车")
    @allure.story("购物车外")
    @allure.title("从首页将商品加入购物车")
    def test_shop_005(self, browser):
        driver = browser
        home = Home(driver)
        home.scroll_first_goods()
        log.info("滚动到第一个商品可见")
        home.click_first_goods()
        log.info("点击第一个商品")
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_add_car()
        log.info("点击加入购物车")
        shopcar = ShopCar(driver)
        assert shopcar.find_quantity_all() > 0

    @allure.feature("购物车")
    @allure.story("购物车外")
    @allure.title("没有登录从首页将商品加入购物车")
    def test_shop_006_skip_login(self, browser):
        driver = browser
        Event.event_add_car(driver)
        text = driver.find_alert_text()
        assert text == '你还未登录!'

    @allure.feature("购物车")
    @allure.story("购物车内")
    @allure.title("勾选购物车中的商品")
    def test_shop_007(self, browser):
        driver = browser
        Event.event_add_car(driver)
        shopcar = ShopCar(driver)
        # 计算并返回所有商品金额
        sum_money = shopcar.sum_money()
        sum_money2 = shopcar.find_total()
        log.info(f"计算金额为：{sum_money},页面金额为：{sum_money2}")
        assert sum_money == sum_money2

    @allure.feature("购物车")
    @allure.story("购物车内")
    @allure.title("删除购物车中的商品")
    def test_shop_008(self, browser):
        driver = browser
        Event.event_add_car(driver)
        shopcar = ShopCar(driver)
        quantity1 = shopcar.find_quantity_all()
        shopcar.click_delete()
        quantity2 = shopcar.find_quantity_all()
        assert quantity1 > quantity2

    @allure.feature("购物车")
    @allure.story("购物车内")
    @allure.title("加减购物车中的商品数量")
    def test_shop_009(self, browser):
        driver = browser
        Event.event_add_car(driver)
        shopcar = ShopCar(driver)
        text1 = shopcar.find_good_quantity()
        shopcar.click_quantity_up()
        text2 = shopcar.find_good_quantity()
        assert text1 < text2
        log.info(f"点击前数量：{text1},点击后数量：{text2}")

    @allure.feature("购物车")
    @allure.story("购物车内")
    @allure.title("购物车中没有商品时不能提交订单")
    def test_shop_010(self, browser):
        driver = browser
        Event.event_add_car(driver)
        sleep(0.2)
        Event.event_add_car(driver)
        shopcar = ShopCar(driver)
        text1 = shopcar.find_good_quantity()
        shopcar.click_quantity_down()
        text2 = shopcar.find_good_quantity()
        assert text1 > text2
        log.info(f"点击前数量：{text1},点击后数量：{text2}")

    @allure.feature("订单")
    @allure.story("立即购买")
    @allure.title("立即购买提交订单")
    def test_shop_011(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_buy_now()
        order = Order(driver)
        log.info(f"收货地址为：{order.find_address()}")
        array1 = order.find_order_details()
        total1 = order.find_total()
        order.click_now_pay()
        usercenter = UserCenter(driver)
        order_state = usercenter.find_order_state()
        array2 = usercenter.find_order_details()
        total2 = usercenter.find_order_total()
        log.info(f"订单状态：{order_state},订单金额：{total1},个人中心金额：{total2}\n订单页面商品：{array1}\n个人中心商品：{array2}")
        assert order_state == "已支付" and total1 == total2 and array1 == array2

    @allure.feature("订单")
    @allure.story("立即购买")
    @allure.title("无收货地址立即购买提交订单")
    def test_shop_012(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_buy_now()
        order = Order(driver)
        log.info(f"收货地址为：{order.find_address()}")
        assert order.find_address() == ''

    @allure.feature("订单")
    @allure.story("加入购物车")
    @allure.title("单商品加入购物车提交订单")
    def test_shop_013(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_add_car()
        shopcar = ShopCar(driver)
        shopcar.click_check_all()
        shopcar.click_buy()
        order = Order(driver)
        array1 = order.find_order_details()
        total1 = order.find_total()
        order.click_now_pay()
        usercenter = UserCenter(driver)
        order_state = usercenter.find_order_state()
        array2 = usercenter.find_order_details()
        total2 = usercenter.find_order_total()
        log.info(f"订单状态：{order_state},订单金额：{total1},个人中心金额：{total2}\n订单页面商品：{array1}\n个人中心商品：{array2}")
        assert order_state == "已支付" and total1 == total2 and array1 == array2

    @allure.feature("订单")
    @allure.story("加入购物车")
    @allure.title("多商品加入购物车提交订单")
    def test_shop_014(self, browser):
        driver = browser
        Event.event_good_details(driver)
        goodsdetails = GoodsDetails(driver)
        goodsdetails.click_add_car()
        Event.event_good_details2(driver)
        goodsdetails.click_add_car()
        shopcar = ShopCar(driver)
        shopcar.click_check_all()
        shopcar.click_buy()
        order = Order(driver)
        array1 = order.find_order_details()
        total1 = order.find_total()
        order.click_now_pay()
        usercenter = UserCenter(driver)
        order_state = usercenter.find_order_state()
        array2 = usercenter.find_order_details()
        total2 = usercenter.find_order_total()
        log.info(f"订单状态：{order_state},订单金额：{total1},个人中心金额：{total2}\n订单页面商品：{array1}\n个人中心商品：{array2}")
        assert order_state == "已支付" and total1 == total2 and array1 == array2 and len(array2) > 1

    @allure.feature("订单")
    @allure.story("加入购物车")
    @allure.title("购物车没有商品提交订单")
    def test_shop_015(self, browser):
        with allure.step("打开购物车0商品提交订单"):
            driver = browser
            sleep(0.2)
            driver.get_url(ENV.shopcar)
            shopcar = ShopCar(driver)
            log.info(f"结算按钮是否可点：{not shopcar.find_buy()}")
        with allure.step("断言"):
            assert shopcar.find_buy()


if __name__ == '__main__':
    # pytest.main(['-vs', 'test_car_order.py::TestCarOrder::test_shop_005'])
    pytest.main(['-vs', 'test_car_order.py::TestCarOrder::test_shop_015', '--clean-alluredir', '--alluredir=../../allure_result'])
    os.system(r"allure generate ../../allure_result -o ../../allure_page -c")
