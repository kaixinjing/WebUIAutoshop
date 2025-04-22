import pymysql
from WebUIAutoshop.common.log import log
from WebUIAutoshop.settings import DBSql


class MysqlAuto(object):
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = pymysql.connect(host=DBSql.database_ip, user=DBSql.database_user, password=DBSql.database_password,
                                        database=DBSql.database_name, charset='utf8mb4')
            self.cursor = self.conn.cursor()
            log.info(f'连接数据库：{DBSql.database_ip}/{DBSql.database_name}')
        except Exception as e:
            log.error(f'数据库连接失败：{e}')

    def __del__(self):
        # 关闭游标和连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        log.info('关闭数据库')

    def execute(self, sql_list, name):
        if not self.cursor:
            log.error('数据库游标未初始化，无法执行 SQL 语句')
            return
        try:
            with self.conn.cursor() as cursor:
                self.conn.begin()
                for i in sql_list:
                    log.info(f'sql：{i}')
                    self.cursor.execute(i, name)
                    log.debug(self.cursor.fetchall())
                    self.conn.commit()
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            log.error(f'执行sql出现错误，异常为{e}')
            raise e


if __name__ == '__main__':
    # MysqlAuto().execute(["select * from shop_user where user_name = %s"], 'test')
    MysqlAuto().execute(DBSql.sql_list, DBSql.test_name)
