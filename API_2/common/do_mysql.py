# -*- coding: utf-8 -*-
# @Time     :2019/4/22  10:25
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :do_mysql.py
import pymysql

class DoMysql:
    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        #self.cursor=self.mysql.cursor()
        #设置返回字典格式,创建字典格式的游标
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()#强制执行最新的
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    mysql=DoMysql()
    result=mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    result1=mysql.fetch_all('select mobilephone from future.member')
    print(result1)
    mysql.close()