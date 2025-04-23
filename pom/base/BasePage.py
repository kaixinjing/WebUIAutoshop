import os
from time import sleep
import allure
from WebUIAutoshop.common.log import log
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

from WebUIAutoshop.config.conf import ALLURE_IMG_DIR


class BasePage:
    def __init__(self, browser=None):
        try:
            if browser:
                self.driver = browser
            else:
                service = Service(r'D:\JetBrains\Chromedrive\chromedriver.exe')
                self.driver = webdriver.Chrome(service=service)
                self.driver.implicitly_wait(10)
                self.driver.maximize_window()

                # 初始化
                # MysqlAuto().execute()
        except Exception as e:
            log.error(f"初始化失败：{e}")
            raise

    # 打开网页
    def get_url(self, url):
        try:
            self.driver.get(url)
            return self.driver
        except Exception as e:
            log.error(f"打开网页失败：{e}")
            raise

    # 退出
    def quit_browser(self):
        try:
            self.driver.quit()
        except Exception as e:
            log.error(f"退出driver失败：{e}")
            raise

    # 截图(元素位置，图片名称)用于验证码
    def get_screenshot(self, selector, code_img_name):
        self.find_element(selector).screenshot(code_img_name)

    # 输入值(元素位置，文本)
    def send_keys(self, selector, context):
        self.find_element(selector).clear()
        sleep(0.2)
        self.find_element(selector).send_keys(context)
        selen = re.sub('[^\u4e00-\u9fa5]+', '', str(selector))
        if len(selen) > 0:
            log.info(f"点击：{selector}，并输入：{context}")
        return True

    # 拿到alert值
    def find_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            text = alert.text
            log.info(text)
            alert.accept()
            return text
        except Exception as e:
            log.error(f"获取alert值失败：{e}")
            raise

    # 点击弹窗的确定
    def click_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            log.error(f"操作弹窗失败：{e}")
            raise

    # 找到元素
    def find_element(self, selector, timeout=10, retries=1):
        for attempt in range(retries):
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(selector)
                )
            except (TimeoutException, NoSuchElementException) as e:
                log.error(f"重试 {attempt + 1} 次")
                if attempt < retries - 1:
                    time.sleep(1)  # 等待1秒后重试
                else:
                    log.error(f"Element 不存在 after {retries} attempts: {selector}")
                    # raise
        return None

    # 找到多个元素
    def find_elements(self, selector, timeout=10, retries=1):
        for attempt in range(retries):
            try:
                return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_all_elements_located(selector)
                )
            except (TimeoutException, NoSuchElementException) as e:
                log.error(f"重试 {attempt + 1} ")
                if attempt < retries - 1:
                    time.sleep(1)  # 等待1秒后重试
                else:
                    log.error(f"Element 不存在 after {retries} attempts: {selector}")
                    # raise
        return None

    # 得到元素text文本
    def get_text(self, selector):
        ele = self.find_element(selector)
        if ele is None:
            return None
        else:
            return ele.text

    # 单击
    def click(self, selector):
        self.find_element(selector).click()
        selen = re.sub('[^\u4e00-\u9fa5]+', '', str(selector))
        if len(selen) > 0:
            log.info(f"点击：{selen}")
        return True

    # 判断元素是否可点击
    def find_is_enabled(self, selector):
        is_enabled = self.find_element(selector).is_enabled()
        return is_enabled

    # 悬停
    def hover(self, selector):
        try:
            mouse = self.find_element(selector)
            ActionChains(self.driver).move_to_element(mouse).perform()
        except NoSuchElementException as e:
            log.error(selector[1] + "找不到元素口牙!" + str(e))

    # 鼠标滚动
    def scroll(self, selector):
        try:
            scroll = self.find_element(selector)
            ActionChains(self.driver).scroll_to_element(scroll).perform()
        except NoSuchElementException as e:
            log.error(selector[1] + "找不到元素口牙!" + str(e))

    # 滚动到指定元素可见
    def scroll_ele(self, selector):
        try:
            ele = self.find_element(selector)
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            self.driver.execute_script('window.scrollBy(0,-200)')
        except NoSuchElementException as e:
            log.error(selector[1] + "找不到元素口牙!" + str(e))

    # chrome自带截图功能
    @allure.step('chrome自带截图')
    def chrome_save_screenshot(self):
        try:
            # conf里的allure路径
            img_dir = ALLURE_IMG_DIR
            str_time = str(time.time())[:10]
            # 图片命名规则，加时间戳
            img_file = ALLURE_IMG_DIR + f'\\allure_screenshot{str_time}.jpg'
            if not os.path.isdir(img_dir):
                os.makedirs(img_dir)
                log.info(f'创建目录：{img_dir}')
            sleep(1)
            self.driver.save_screenshot(img_file)
            log.info("网页截图")
            return img_file
        except Exception as e:
            log.error(f'截图异常：{e}')
            raise

    # 失败截图放到allure报告里
    def allure_save_screenshot(self, name):
        with open(self.chrome_save_screenshot(), "rb") as f:
            allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.JPG)
            log.info("将截图放到allure报告里")
