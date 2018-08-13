# -*- coding: UTF-8 -*-
'''
Created on 2018-8-10

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
import coursedetail
from PO.base import Base

class CourseDetailTest(unittest.TestCase):


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
        
    @unittest.skip("test")     
    def test_open_teacher_detail(self):
        mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        coursedetail.click_first_tab(self.driver, self.cfg)
        base = Base(self.driver)
        base.swipeUp(0.75,0.5,500)
        flag = coursedetail.open_teacher_info(self.driver, self.cfg, 0)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.assertTrue(flag, u"打开老师详情页错误")
        self.driver.switch_to.context("NATIVE_APP")
        
    @unittest.skip("test")    
    def test_open_school_home(self):
        mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        coursedetail.click_first_tab(self.driver, self.cfg)
        base = Base(self.driver)
        base.swipeUp(0.75,0.25,500)
        flag = coursedetail.open_org_info(self.driver, self.cfg)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.assertTrue(flag, u"打开机构首页错误")
        self.driver.switch_to.context("NATIVE_APP")
        
    def test_open_course_tag(self):
        mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        coursedetail.click_first_tab(self.driver, self.cfg)
        base = Base(self.driver)
        base.swipeUp(0.75,0.25,500)
        base.swipeUp(0.75,0.5,500)
        flag = coursedetail.open_course_tag(self.driver, self.cfg)
        self.assertTrue(flag, u"点击课程标签错误")
        
    def tearDown(self):
        time.sleep(2)
        coursedetail.click_back_btn(self.driver, self.cfg)
        
        mycourse.click_back_btn(self.driver, self.cfg)
        
        login.logout_by_exit_btn(self.driver, self.cfg)
        self.driver.quit()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suite_mycenter = unittest.TestLoader().loadTestsFromTestCase(CourseDetailTest)
    
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