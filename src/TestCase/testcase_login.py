# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver
import HTMLTestRunner
import login

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

class LoginTest(unittest.TestCase):

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
        
        
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
                                     
        self.mobile_num = self.cfg.get('env_para', 'mobile_num')
        self.mobile_pwd = self.cfg.get('env_para', 'mobile_pwd')
        
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')
        
        self.email_num = self.cfg.get('env_para', 'email_num')
        self.email_pwd = self.cfg.get('env_para', 'email_pwd')
    
     
    def test_loginby_username(self):
        text = login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        self.assertTrue(u"登录/注册" != text, u"用户名登录错误")
        login.logout_by_exit_btn(self.driver, self.cfg)
        
    @unittest.skip("test")     
    def test_loginby_mobile(self):
        text = login.login_by_mobile(self.cfg, self.driver, self.mobile_num, self.mobile_pwd)
        self.assertTrue(u"登录/注册" != text, u"手机号登录错误")
        login.logout_by_exit_btn(self.driver, self.cfg)
        
    @unittest.skip("test") 
    def test_loginby_email(self):
        text = login.login_by_email(self.cfg, self.driver, self.email_num, self.email_pwd)
        self.assertTrue(u"登录/注册" != text, u"邮箱登录错误")
        login.logout_by_exit_btn(self.driver, self.cfg)
      
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    
    
    suite_login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    
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


    
