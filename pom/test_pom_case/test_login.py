import os
import subprocess
import allure
import pytest
from WebUIAutoshop.common.yaml import get_yaml_data
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.settings import ENV
from WebUIAutoshop.pom.page.Home import Home
from WebUIAutoshop.pom.page.Login import Login
from WebUIAutoshop.pom.base.Event import Event


class TestLogin:
    @pytest.mark.parametrize(
        'case',
        get_yaml_data('data.yaml', 'test_login'),
        ids=lambda case: case['name']
    )
    @allure.feature("登录与注册")
    @allure.story("登录")
    @allure.title("三种情况登录测试{case[name]}")
    def test_shop_001(self, case, browser):
        driver = browser
        driver.get_url(ENV.url)
        home = Home(driver)
        login = Login(driver)
        usercenter = UserCenter(driver)
        home.click_login_btn()
        username = case['username']
        password = case['password']
        result = case['result']
        code = case['code']

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
    pytest.main(['-vs', 'test_login.py::TestLogin::test_shop_001', '--clean-alluredir', '--alluredir=../../allure_result'])
    os.system(r"allure generate ../../allure_result -o ../../allure_page -c")
    subprocess.Popen(r"allure open ../../allure_page", shell=True)