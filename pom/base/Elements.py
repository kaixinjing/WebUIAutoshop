from selenium.webdriver.common.by import By


class Elements:
    home_login_btn = (By.XPATH, "//a[@id='login']")
    login_user_inp = (By.XPATH, "//input[@placeholder='请输入用户名']")
    login_pw_inp = (By.XPATH, "//input[@placeholder='请输入密码']")
    login_code_inp = (By.XPATH, "//input[@placeholder='验证码']")
    login_code_img = (By.XPATH, "//img[@onclick='changeCode(this)']")
    login_login_btn = (By.XPATH, "//input[@type='submit']")
    
