# -*- coding: UTF-8 -*-
'''
Created on 2018-8-15

@author: ablesky
'''
import unittest

from appium import webdriver
import HTMLTestRunner

import mycollect

import login
from PO.index_page import Index

import time

from PO.personal_page import Personal

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

class MyCollectPageTest(unittest.TestCase):


    def setUp(self):
        cfgfile = "..\config\config.ini"
        
        self.cfg = ConfigParser.ConfigParser()
        '''
        self.cfg.read('..\config\config.ini')
        '''
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
        
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')
        
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        
        self.index = Index(self.driver, self.cfg)
        self.index.click_tab_myself_btn()
        
        self.personal = Personal(self.driver, self.cfg)
        print u"打开我的收藏"
        self.personal.click_my_collect()
        
    
    #从我的收藏进入课程详情页取消收藏课程 
    @unittest.skip("test")
    def test_abolish_thecourse_of_collection_in_coursedetail(self):
        ifabolish = mycollect.abolish_the_course_of_collection_in_coursedetail(self.driver, self.cfg,0)
        self.assertTrue(ifabolish, u'课程取消收藏失败')
    
    #清空收藏列表 
    @unittest.skip("test")  
    def test_clear_collect_list(self):
        noDataFlag = mycollect.click_sure_btn_after_open_clear_dlg(self.driver, self.cfg)
        self.assertTrue("暂时没有收藏" == noDataFlag, u'清空收藏列表失败')
    
    #取消收藏列表
    @unittest.skip("test")
    def test_cancel_clear_collect_list(self):
        cancelClearFlag = mycollect.click_cancel_btn_after_open_clear_dlg(self.driver, self.cfg)
        self.assertTrue(cancelClearFlag, u"取消清空收藏失败")
        
    #在我的收藏页面长按课程取消收藏课程
    @unittest.skip("test")
    def test_abolish_the_first_course_of_collection_by_longclick(self):
        cancelAbolishSuccess = mycollect.abolish_the_course_of_collection_by_longclick(self.driver, self.cfg,0)
        
        self.assertTrue(1 == cancelAbolishSuccess, u"长按取消收藏课程失败")
    
    def test_my_collect_page(self):
        #从我的收藏进入课程详情页取消收藏课程 
        ifabolish = mycollect.abolish_the_course_of_collection_in_coursedetail(self.driver, self.cfg,0)
        self.assertTrue(ifabolish, u'课程取消收藏失败')
        
        #在我的收藏页面长按课程取消收藏课程
        cancelAbolishSuccess = mycollect.abolish_the_course_of_collection_by_longclick(self.driver, self.cfg,0)
        self.assertTrue(1 == cancelAbolishSuccess, u"长按取消收藏课程失败")
        
        #取消收藏列表
        cancelClearFlag = mycollect.click_cancel_btn_after_open_clear_dlg(self.driver, self.cfg)
        self.assertTrue(cancelClearFlag, u"取消清空收藏失败")
        
        #清空收藏列表
        noDataFlag = mycollect.click_sure_btn_after_open_clear_dlg(self.driver, self.cfg)
        self.assertTrue("暂时没有收藏" == noDataFlag, u'清空收藏列表失败')
        
    def tearDown(self):
        time.sleep(2)
        mycollect.click_back_btn(self.driver, self.cfg)
        login.logout_by_exit_btn(self.driver, self.cfg)
        
        self.driver.quit()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite_mycenter = unittest.TestLoader().loadTestsFromTestCase(MyCollectPageTest)
    
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