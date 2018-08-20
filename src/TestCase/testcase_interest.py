# -*- coding: UTF-8 -*-
'''
Created on 2018-8-16

@author: ablesky
'''
import unittest

from appium import webdriver
import HTMLTestRunner

import login
from PO.index_page import Index

import time

from PO.personal_page import Personal

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

from PO.setting_page import Setting
import interest

class InterestTest(unittest.TestCase):
    
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
        desired_caps['unicodeKeyboard'] = self.cfg.get('env_para', 'unicodeKeyboard')
        desired_caps['resetKeyboard'] = self.cfg.get('env_para', 'resetKeyboard')
        desired_caps['automationName'] = self.cfg.get('env_para', 'automationName')
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
        
        time.sleep(3)
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')
        
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        
        self.index = Index(self.driver, self.cfg)
        self.index.click_tab_myself_btn()
        
        self.personal = Personal(self.driver, self.cfg)
        print u"打开设置"
        self.personal.click_setting()
        self.setting = Setting(self.driver, self.cfg)
        print u"打开修改兴趣页面"
        self.setting.click_set_interest_item()
        
    def test_modify_interest(self):
        interest.choose_interest(self.driver, self.cfg)
        #self.assertTrue(flag, u"修改兴趣失败")
        self.setting.click_logout_btn()
        
    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    
    
    suite_login = unittest.TestLoader().loadTestsFromTestCase(InterestTest)
    
    allsuites = []
    allsuites.append(suite_login)
    alltests = unittest.TestSuite(allsuites)
    
    
    fp = open("../report/myreport.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(alltests)
