# -*- coding: utf-8 -*-
# @Time     :2019/3/18  9:44
# @Author   :liying
# @Email    :1025452202@qq.com
# @File     :config_a.py


from configparser import ConfigParser

class myConfig:
    def __init__(self,filepath,encoding='utf-8'):
        self.cf=ConfigParser()
        self.cf.read(filepath,encoding)
#获取整数
    def get_intValue(self,section,option):
        return self.cf.getint(section,option)
#获取布尔值
    def get_boolValue(self,section,option):
        return self.cf.getboolean(section,option)
#获取字符串
    def get_strValue(self,section,option):
        return self.cf.get(section,option,raw=True)
#获取浮点数
    def get_floatValue(self,section,option):
        return self.cf.getfloat(section,option)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self,section):
        return self.cf.options(section)

if __name__ == '__main__':
    mf=myConfig('online.cfg')
    print(mf.get_strValue('api','pre_url'))
    # print(mf.get_boolValue('excel','bool_num'))
    # print(mf.get_floatValue('excel','num'))
    # print(mf.get_intValue('db','db_port'))
    # print(mf.get_strValue('per_info','sex'))
    # print(mf.get_sections())
    # print(mf.get_options('excel'))



