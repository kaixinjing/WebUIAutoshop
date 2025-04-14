# 存放配置信息
class ENV:
    # 环境
    url = 'http://localhost:8080/shop/GetCategory'
    UserCenter = 'http://localhost:8080/shop/GetUser'
    login = 'http://localhost:8080/shop/login.jsp'
    gooddetails = 'http://localhost:8080/shop/GetProductDetail?id=44'
    gooddetails2 = 'http://localhost:8080/shop/GetProductDetail?id=45'
    shopcar = 'http://localhost:8080/shop/GetCart'


class DBSql:
    database_ip = 'localhost'
    database_name = 'shop'
    database_user = 'root'
    database_password = 'root'
    test_name = 'test'
    sql_list = [
        "delete from shop_orderitem where order_id = (select order_id from shop_order where user_id = (SELECT user_id FROM shop_user WHERE user_name = %s))",
        "delete from shop_cart where user_id = (SELECT user_id FROM shop_user WHERE user_name = %s)",
        "delete from shop_order where user_id = (SELECT user_id FROM shop_user WHERE user_name = %s)",
        "delete from shop_user where user_name = %s",
        "INSERT INTO shop_user (user_id, user_name, user_password, user_phone, user_email, user_address, user_status) VALUES(5, %s, '000', '123456', '123@qq.com', '门头沟', 0)"
    ]
