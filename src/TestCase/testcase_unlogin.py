# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''


import unittest
from appium import webdriver
import HTMLTestRunner, time
import login
from PO.index_page import Index
from PO.personal_page import Personal
import home

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

class UnLoginTest(unittest.TestCase):

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
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
        
    #未登录情况下点击个人中心的快速入口                                  
    def test_click_the_quick_entry_of_the_personal_center_without_loggin_in(self):
        print u'首页有广告先关闭广告，否则直接点击我的进入个人中心'
        try:
            home.close_the_suspended_advertisement(self.driver,self.cfg)
        except:
            pass
        index = Index(self.driver,self.cfg)
        index.click_tab_myself_btn()
        personalpage = Personal(self.driver,self.cfg)
        print u'未登录情况下点击我的课程'        
        personalpage.click_my_course()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击我的课程进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击我的收藏'        
        personalpage.click_my_collect()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击我的收藏进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
        
        print u'未登录情况下点击关注网校'        
        personalpage.click_pay_attention_school()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击关注网校进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击我的下载'        
        personalpage.click_my_download()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击我的下载进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击优惠券'        
        personalpage.click_my_coupon()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击优惠券进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击会员'        
        personalpage.click_my_vip()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击会员进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击账户余额'        
        personalpage.click_balance()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击账户余额进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击推荐有奖'        
        personalpage.click_award()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击推荐有奖进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
            
        print u'未登录情况下点击分享收益'        
        personalpage.click_share_earning()
        try:
            title = login.get_login_page_title(self.driver,self.cfg)
            self.assertEqual(title, u'登录', u'未登录情况下点击分享收益进入登录页面失败')
            login.click_back_btn(self.driver,self.cfg)
        except Exception,e:
            print e
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    
    
    suite_login = unittest.TestLoader().loadTestsFromTestCase(UnLoginTest)
    
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
