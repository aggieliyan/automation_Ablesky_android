# -*- coding: UTF-8 -*-
'''
Created on 2018-8-15

@author: ablesky
'''
from PO.base import Base
import time
from appium.webdriver.common.touch_action import TouchAction

class MyCollectPage(Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg

    
    def click_back_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_back_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_back_btn')).click()
    
    def click_clear_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_clear_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_clear_btn')).click()
    
    def click_clear_dlg_sure_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_clear_dlg_sure_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_clear_dlg_sure_btn')).click()
    
    def click_clear_dlg_cancel_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_clear_dlg_cancel_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_clear_dlg_cancel_btn')).click()
    
    
    def get_collectcourse_list(self):
        time.sleep(5)
        collectcourselist = self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_course_list_by'), \
                             self.cfg.get('my_collect_page', 'my_collect_page_course_list'))
        collectcourselistitems = collectcourselist.find_elements(self.cfg.get('my_collect_page', 'my_collect_page_course_list_item_by'), \
                                                                 self.cfg.get('my_collect_page', 'my_collect_page_course_list_item'))
        return collectcourselistitems
    
    def get_collectcourse_list_length(self,list):
        listlen = len(list)
        return listlen
                                  
    def click_collectcourseitem(self,list,item):
        time.sleep(2)
        list[item].click()
        
    def longClick_collectcourseitem(self,list,item):
        time.sleep(2)
        TouchAction(self.dr).long_press(list[item]).perform()
        
    def click_cancel_abolish_dlg_cancel_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_cancel_abolish_dlg_cancel_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_cancel_abolish_dlg_cancel_btn')).click()
     
    def click_cancel_abolish_dlg_sure_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_cancel_abolish_dlg_sure_btn_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_cancel_abolish_dlg_sure_btn')).click()
     
        
    def get_list_titles(self):
        time.sleep(2)
        collectcourselist = self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_course_list_by'), \
                             self.cfg.get('my_collect_page', 'my_collect_page_course_list'))
        list = collectcourselist.find_elements(self.cfg.get('my_collect_page', 'my_collect_page_course_title_by'), \
                                                                      self.cfg.get('my_collect_page', 'my_collect_page_course_title'))
        collectlisttitles = []
        i = 0       
        while i < len(list):
            collectlisttitles.append(list[i].text)
            i = i + 1
        
        return collectlisttitles
    
    def get_list_no_data_flag(self):
        time.sleep(2)
        noDataFlag = self.dr.find_element(self.cfg.get('my_collect_page', 'my_collect_page_no_data_by'), \
                              self.cfg.get('my_collect_page', 'my_collect_page_no_data')).text
        return noDataFlag

        