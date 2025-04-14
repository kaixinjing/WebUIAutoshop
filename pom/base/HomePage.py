from WebUIAutoshop.pom.base.BasePage import BasePage

# conftest里的全局变量driver，调用了这个类，构造方法调用了BasePage的构造方法实例化了driver对象
class HomePage(BasePage):

    def __init__(self):
        super().__init__()
