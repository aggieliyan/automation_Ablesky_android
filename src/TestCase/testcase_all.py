# -*- coding: UTF-8 -*-
'''
Created on 2018-8-28

@author: ablesky
'''
import unittest
from appium import webdriver
import HTMLTestRunner
import login
import time
import TestCase
from PO.index_page import Index

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

class AllTestCaseTest(unittest.TestCase):


    def setUp(self):
        cfgfile = "..\config\config.ini"
        
        self.cfg = ConfigParser.ConfigParser()
        
        self.cfg.readfp(codecs.open(cfgfile, "r", "gb2312"))
        
        desired_caps = {}
        desired_caps['platformName'] = self.cfg.get('env_para', 'platformName')
        desired_caps['platformVersion'] = self.cfg.get('env_para', 'platformVersion')
        desired_caps['appPackage'] = self.cfg.get('env_para', 'appPackage')
        desired_caps['appActivity'] = self.cfg.get('env_para', 'appActivity')
        desired_caps['deviceName'] = self.cfg.get('env_para', 'deviceName')
        #desired_caps['unicodeKeyboard'] = self.cfg.get('env_para', 'unicodeKeyboard')
        #desired_caps['resetKeyboard'] = self.cfg.get('env_para', 'resetKeyboard')
        
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
        
        time.sleep(3)
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')        
    
    #测试详情页相关内容及播放下载 
    def testCourseDetail(self):
        print u"用户名登录"
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        TestCase.testCourseDetail(self,self.driver, self.cfg)
        time.sleep(2)
        index = Index(self.driver, self.cfg)
        index.click_tab_myself_btn()
        #退出登录
        login.logout_by_exit_btn(self.driver, self.cfg)
    
    #测试我的课程相关内容 
    def testMyCoursePage(self):
        print u"用户名登录"
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        TestCase.testMyCoursePage(self,self.driver, self.cfg)
        time.sleep(2)
        index = Index(self.driver, self.cfg)
        index.click_tab_myself_btn()
        login.logout_by_exit_btn(self.driver, self.cfg)
    
    #测试我的收藏相关内容    
    def testMyCollectPage(self):
        print u"用户名登录"
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        TestCase.testMyCollectPage(self,self.driver, self.cfg)
        time.sleep(2)
        index = Index(self.driver, self.cfg)
        index.click_tab_myself_btn()
        login.logout_by_exit_btn(self.driver, self.cfg)
    
    #测试未登录情况下相关操作
    def testOperateWithoutLogin(self):
        TestCase.testOperateWithoutLogin(self,self.driver, self.cfg)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite_mycenter = unittest.TestLoader().loadTestsFromTestCase(AllTestCaseTest)
    
    allsuites = []
    allsuites.append(suite_mycenter)
    alltests = unittest.TestSuite(allsuites)
    
    
    fp = open("../report/myreport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(alltests)