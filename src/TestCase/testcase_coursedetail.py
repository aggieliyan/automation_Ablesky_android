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

import play

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
        #desired_caps['unicodeKeyboard'] = self.cfg.get('env_para', 'unicodeKeyboard')
        #desired_caps['resetKeyboard'] = self.cfg.get('env_para', 'resetKeyboard')
        
        self.adds = self.cfg.get('env_para', 'adds')
        self.driver = webdriver.Remote(self.adds, desired_caps)
        
        time.sleep(3)
        self.username_num = self.cfg.get('env_para', 'username_num')
        self.username_pwd = self.cfg.get('env_para', 'username_pwd')
        
        print u"用户名登录"
        login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
        
        self.index = Index(self.driver, self.cfg)
        self.index.click_tab_myself_btn()
        
        self.personal = Personal(self.driver, self.cfg)
        print u"打开我的课程"
        self.personal.click_my_course()
        
        
    @unittest.skip("test")
    def test_play_video(self):
        print u"开始测试播放单视频..."
        mycourse.search_course_and_open_the_course_detail(self.driver, self.cfg)
        coursedetail.click_second_tab(self.driver, self.cfg)
        coursedetail.play_courseware(self.driver, self.cfg,0)
        play.play_video_and_exist(self.driver, self.cfg)
        self.driver.press_keycode(4)
        mycourse.click_back_btn(self.driver, self.cfg)
        
    def test_download_all_coursewares(self):
        print u"开始测试下载课件..."
        mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        coursedetail.download_all_courseware(self.driver, self.cfg)
        mycourse.click_back_btn(self.driver, self.cfg)
        self.personal.click_my_download()
        time.sleep(5)
        self.driver.press_keycode(4)
        
    @unittest.skip("test")   
    def test_course_detail(self): 
        mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
        coursedetail.click_first_tab(self.driver, self.cfg)
        base = Base(self.driver)
        print u"开始测试打开老师详情..."
        base.swipeUp(0.75,0.5,500)
        try:
            flag = coursedetail.open_teacher_info(self.driver, self.cfg, 0)
            time.sleep(2)
            self.driver.press_keycode(4)
            self.assertTrue(flag, u"打开老师详情页错误")
            base.switchToNative()
            base.shutdownChromeDriver()
        except:
            print u"课程详情没有设置老师信息"
        
        
        print u"开始测试打开机构首页"
        coursedetail.click_first_tab(self.driver, self.cfg)
        base.swipeUp(0.75,0.5,500)
        flag = coursedetail.open_org_info(self.driver, self.cfg)       
        time.sleep(2)
        self.driver.press_keycode(4)
        self.assertTrue(flag, u"打开机构首页错误")
        base.switchToNative()
        base.shutdownChromeDriver()
        
        print u"开始测试课程标签"
        coursedetail.click_first_tab(self.driver, self.cfg)
        try:
            base.swipeUp(0.75,0.5,500)
            flag = coursedetail.open_course_tag(self.driver, self.cfg)
            self.assertTrue(flag, u"点击课程标签错误")
        except:
            print u"课程详情没有设置标签"
        
        
        print u"开始测试点击底部推荐课程"
        coursedetail.click_first_tab(self.driver, self.cfg)
        base.swipeUp(0.75,0.5,500)
        try:
            flag = coursedetail.click_bottom_recommend_course(self.driver, self.cfg,0)
            self.assertTrue(flag, u"点击底部推荐课程错误")
        except:
            print u"课程详情没有推荐课程"
        coursedetail.click_back_btn(self.driver, self.cfg)    
        mycourse.click_back_btn(self.driver, self.cfg)
        
        
        
    def tearDown(self):
        time.sleep(2)
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