import ddddocr
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, browser):
        self.driver = browser
        self.user_inp = (By.XPATH, "//input[@placeholder='请输入用户名']")
        self.pw_inp = (By.XPATH, "//input[@placeholder='请输入密码']")
        self.code_inp = (By.XPATH, "//input[@placeholder='验证码']")
        self.code_img = (By.XPATH, "//img[@onclick='changeCode(this)']")
        self.login_btn = (By.XPATH, "//input[@type='submit']")
        self.register_btn = (By.XPATH, "//a[contains(text(),'免费注册')]")
        self.name = (By.XPATH, "//h2[contains(text(),'用户登录')]")
        self.user_error = (By.XPATH, "/html/body/div/form/p[1]/span")
        self.pw_error = (By.XPATH, "/html/body/div/form/p[2]/span")
        self.code_error = (By.XPATH, "/html/body/div/form/p[3]/span")

    # 输入用户名
    def input_user(self, name):
        self.driver.send_keys(self.user_inp, name)

    # 输入密码
    def input_password(self, password):
        self.driver.send_keys(self.pw_inp, password)

    # 验证码截图
    def screenshot_code(self):
        self.driver.get_screenshot(self.code_img, "code.png")

    # 输入验证码
    def input_code(self, code=None):
        if code:
            self.driver.send_keys(self.code_inp, code)
        else:
            while 1:
                self.driver.click(self.code_img)
                self.screenshot_code()
                ocr = ddddocr.DdddOcr()
                with open("code.png", "rb") as fp:
                    image = fp.read()
                catch = ocr.classification(image)
                self.driver.send_keys(self.code_inp, catch)
                self.driver.click(self.name)
                text = self.driver.get_text(self.code_error)
                if "验证码" in text:
                    continue
                else:
                    break

    # 点击登录按钮
    def click_login_btn(self):
        self.driver.click(self.login_btn)

    # 点击免费注册按钮
    def click_register_btn(self):
        self.driver.click(self.register_btn)
