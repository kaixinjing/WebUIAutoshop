from time import sleep
import allure
from WebUIAutoshop.common.log import log
from WebUIAutoshop.pom.page.GoodsDetails import GoodsDetails
<<<<<<< HEAD
=======
from WebUIAutoshop.pom.page.Home import Home
>>>>>>> b0c550d611f6f8e2440119172c9ea705be8e13e0
from WebUIAutoshop.pom.page.Login import Login
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.settings import ENV


class Event:
    @staticmethod
    @allure.title("登录操作")
    def event_login(browser, username, password, code):
        try:
            browser.get_url(ENV.login)
            login = Login(browser)
            login.input_user(username)
            login.input_password(password)
            login.input_code(code)
            login.click_login_btn()
<<<<<<< HEAD
=======
            home = Home(browser)
            assert "你好" in home.find_login_msg()
>>>>>>> b0c550d611f6f8e2440119172c9ea705be8e13e0
        except Exception as e:
            log.error(f'登录异常：{e}')

    @staticmethod
    @allure.title("退出登录操作")
    def event_login_quit(browser):
        try:
            browser.get_url(ENV.UserCenter)
            usercenter = UserCenter(browser)
            usercenter.click_user_quit()
        except Exception as e:
            log.error(f'退出登录异常：{e}')

    @staticmethod
    def register():
        pass

    @staticmethod
    @allure.title("进入商品详情页操作")
    def event_good_details(browser):
        try:
            driver = browser
            sleep(0.2)
            driver.get_url(ENV.gooddetails)
            log.info("进入商品详情页")
        except Exception as e:
            log.error(f'进入商品详情页异常：{e}')

    @staticmethod
    @allure.title("进入商品详情页操作")
    def event_good_details2(browser):
        try:
            driver = browser
            sleep(0.2)
            driver.get_url(ENV.gooddetails2)
            log.info("进入商品详情页")
        except Exception as e:
            log.error(f'进入商品详情页异常：{e}')

    @staticmethod
    @allure.title("将商品加入购物车")
    def event_add_car(browser):
        try:
            driver = browser
            driver.get_url(ENV.gooddetails)
            goodsdetails = GoodsDetails(browser)
            goodsdetails.click_add_car()
            log.info("成功添加商品到购物车")
        except Exception as e:
            log.error(f'商品加入购物车异常：{e}')
