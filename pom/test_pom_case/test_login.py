import allure
import pytest
from WebUIAutoshop.common.log import log
from WebUIAutoshop.pom.page.GoodsDetails import GoodsDetails
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.settings import ENV
from WebUIAutoshop.pom.page.Home import Home
from WebUIAutoshop.pom.page.Login import Login
from WebUIAutoshop.pom.page.ShopCar import ShopCar
from WebUIAutoshop.pom.base.Event import Event


class TestLogin:
    @allure.feature("登录与注册")
    @allure.story("登录")
    @pytest.mark.parametrize('username, password, result, code', [
        ('admin', '000', "你好", None),
        ('hhh', 'hhh', "用户", None),
        ('admin', '000', "验证码", "hhh")
    ], ids=(
        'test_shop_001',
        'test_shop_002',
        'test_shop_003',
    ))
    def test_shop(self, username, password, result, code, browser):
        driver = browser
        home = Home(driver)
        login = Login(driver)
        usercenter = UserCenter(driver)
        driver.get_url(ENV.url)
        home.click_login_btn()
        Event.event_login(driver, username, password, code)
        if "你好" in result:
            text_hellow = driver.get_text(home.login_msg)
            # 进入个人中心
            home.click_user_center()
            # 退出登录
            usercenter.click_user_quit()
            assert "你好" in text_hellow
        elif "用户" in result:
            text_user = driver.get_text(login.user_error)
            assert "用户" in text_user
        elif "验证码" in result:
            text_code2 = driver.get_text(login.code_error)
            assert "验证码" in text_code2


if __name__ == '__main__':
    pytest.main(["-vs"])
