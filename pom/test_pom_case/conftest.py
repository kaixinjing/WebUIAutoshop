import os

import allure
import pytest
import yaml

from WebUIAutoshop.common.log import log
from WebUIAutoshop.common.sql import MysqlAuto
from WebUIAutoshop.common.yaml import get_yaml_data
from WebUIAutoshop.pom.base.Event import Event
from WebUIAutoshop.pom.base.HomePage import HomePage
from WebUIAutoshop.settings import ENV, DBSql
from WebUIAutoshop.config.conf import DATA_YAML

driver = None


@pytest.fixture(scope='class')
@allure.title("打开或关闭浏览器")
def browser():
    global driver
    driver = HomePage()
    log.debug('创建driver对象')
    driver.get_url(ENV.url)
    log.debug('打开浏览器')
    yield driver
    driver.quit_browser()
    log.debug('关闭浏览器')


# @pytest.fixture(scope='function', autouse=True)
# def get_yaml_data(request):
#     marker = request.node.get_closest_marker("get_yaml_data")
#     if not marker:
#         yield
#         return
#     file_path, key = marker.args
#     log.info(f"使用{file_path}数据驱动")
#     path = os.path.join(DATA_YAML, file_path)
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             data = yaml.safe_load(file)
#         test_data = data.get(key, [])
#     except Exception as e:
#         log.error(f"加载YAML数据失败：{e}")
#         test_data = []
#     yield test_data


@pytest.fixture(scope='function', autouse=True)
@allure.title("登录或退出")
def login_and_quit(browser, request):
    """
    fixture装饰的前置登录退出函数，通过函数名来判断是否跳过登录
    :param browser: 浏览器
    :param request: 当前测试函数的详细信息
    :return:
    """
    name = request.node.name
    if "skip_login" in name:
        with allure.step("跳过登录"):
            log.info("跳过登录逻辑")
            yield
            return
    MysqlAuto().execute(DBSql.sql_list, DBSql.test_name)
    user = get_yaml_data('data.yaml', 'test_user')
    Event.event_login(browser, user[0]['username'], user[0]['password'], None)
    log.info("登录成功")
    yield
    Event.event_login_quit(browser)
    log.info("退出登录")


# 定义一个钩子函数，在测试用例执行完毕后捕获结果
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    从yield中获取执行结果，如果在call(调用阶段)且失败了
    则获取失败函数名，传递browser，调用封装的截图函数
    :param item: 测试项对象，包含测试函数的信息
    :param call: 调用对象，包含测试函数的调用信息
    :return: None
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            test_name = item.name
            browser = item.funcargs['browser']
            browser.allure_save_screenshot(test_name)
        except Exception as e:
            log.error(f"allure截图钩子函数报错: {e}")
