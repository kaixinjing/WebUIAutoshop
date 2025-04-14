import pymysql
from WebUIAutoshop.common.log import log
from WebUIAutoshop.settings import DBSql


class MysqlAuto(object):
    def __init__(self):
        self.conn = pymysql.connect(host=DBSql.database_ip, user=DBSql.database_user, password=DBSql.database_password,
                                    database=DBSql.database_name, charset='utf8mb4')
        self.cursor = self.conn.cursor()
        log.info(f'连接数据库：{DBSql.database_ip}/{DBSql.database_name}')

    def __del__(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        log.info('关闭数据库')

    def execute(self, sql_list, name):
        try:
            for i in sql_list:
                log.info(f'sql：{i}')
                self.cursor.execute(i, name)
                log.debug(self.cursor.fetchall())
            # 提交事务
            self.conn.commit()
            return self.cursor.fetchall()
        except Exception as e:
            log.error(f'执行sql出现错误，异常为{e}')
            raise e


if __name__ == '__main__':
    # MysqlAuto().execute(['select * from shop_user'])
    MysqlAuto().execute(DBSql.sql_list, DBSql.test_name)
