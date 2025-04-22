import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "log")
ALLURE_IMG_DIR = os.path.join(LOG_DIR, "image_allure")
DATA_YAML = os.path.join(BASE_DIR, "data")
if __name__ == '__main__':
    print('项目目录：' + BASE_DIR)
    print('数据目录：' + DATA_YAML)
    print('日志目录：' + LOG_DIR)
    print('allure报告截图目录：' + ALLURE_IMG_DIR)
