# -*- coding: UTF-8 -*-
'''
Created on 2018-8-10

@author: ablesky
'''
import unittest
from appium import webdriver
import HTMLTestRunner, time
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import codecs

class InstallTest(unittest.TestCase):

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
                                     
    def test_install_apk(self):
        isInstall = self.driver.is_app_installed("com.ablesky.ui.activity")
        print isInstall
        if(False == isInstall):
            self.driver.install_app("..\app\AbleSky_V8.6_WWW_201808101552.apk")
        self.driver.launch_app()
        time.sleep(2)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    
    
    suite_login = unittest.TestLoader().loadTestsFromTestCase(InstallTest)
    
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


    
