import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "log")
ALLURE_IMG_DIR = os.path.join(LOG_DIR, "image_allure")
<<<<<<< HEAD
DATA_YAML = os.path.join(BASE_DIR, "data")
if __name__ == '__main__':
    print('项目目录：' + BASE_DIR)
    print('数据目录：' + DATA_YAML)
=======
if __name__ == '__main__':
    print('项目目录：' + BASE_DIR)
>>>>>>> b0c550d611f6f8e2440119172c9ea705be8e13e0
    print('日志目录：' + LOG_DIR)
    print('allure报告截图目录：' + ALLURE_IMG_DIR)
