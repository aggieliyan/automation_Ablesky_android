# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
import unittest

from appium import webdriver
import HTMLTestRunner

import mycourse

import login
from PO.index_page import Index

import time

from PO.personal_page import Personal

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

import codecs

class MyCoursePageTest(unittest.TestCase):


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
        desired_caps['unicodeKeyboard'] = self.cfg.get('env_para', 'deviceName')
        desired_caps['resetKeyboard'] = self.cfg.get('env_para', 'unicodeKeyboard')
        desired_caps['automationName'] = self.cfg.get('env_para','resetKeyboard')
        
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
        
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')
        
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        
        time.sleep(2)
        self.index = Index(self.driver, self.cfg)
        time.sleep(2)
        self.index.click_tab_myself_btn()
        time.sleep(2)
        
        self.personal = Personal(self.driver, self.cfg)
        self.personal.click_my_course()
    '''    
    #从我的课程点击进入点播课程详情页
    def test_open_dianbo_coursedetail(self):
        openflag = mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开点播课程失败")
    
    #从我的课程点击进入预售班课程详情页
    def test_open_presell_coursedetail(self):
        openflag = mycourse.click_my_course_page_presell_list_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开预售班课程失败")
        
    #从我的课程点击进入网络班课程详情页
    def test_open_network_coursedetail(self):
        openflag = mycourse.click_my_course_page_network_list_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开网络班课程失败")
       
    #从我的课程点击进入面授班课程详情页
    def test_open_face_coursedetail(self):
        openflag = mycourse.click_my_course_page_face_list_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开面授班课程失败")
        
    #从我的课程点击进入直播课程详情页
    def test_open_live_coursedetail(self):
        openflag = mycourse.click_my_course_page_live_list_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开直播课程失败")
    
    #从我的课程点击进入考试卷开始答题页
    def test_open_examination(self):
        openflag = mycourse.click_my_course_page_examination_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开考试卷失败")
    '''
    
    #从我的课程点击进入练习卷开始答题页
    def test_open_exercise(self):
        openflag = mycourse.click_my_course_page_exercise_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开练习卷失败")
        time.sleep(2)
        mycourse.click_back_btn(self.driver, self.cfg)
        
        login.logout_by_exit_btn(self.driver, self.cfg)
    '''
    #从我的课程点击进入题库开始答题页
    def test_open_question_bank(self):
        openflag = mycourse.click_my_course_page_question_bank_item(self.driver, self.cfg)
        self.assertTrue(openflag, u"打开题库失败")
    '''
    def tearDown(self):
        
        
        self.driver.quit()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite_mycenter = unittest.TestLoader().loadTestsFromTestCase(MyCoursePageTest)
    
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