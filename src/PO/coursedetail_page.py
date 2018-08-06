# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''

from PO.base import Base
import time
import random

class CourseDetailPage(Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg

    
    def click_back_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_back_btn_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_back_btn')).click()
    
    
    
    
    def click_collect_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_collect_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_collect_icon')).click()
    
    
    def click_share_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_share_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_share_icon')).click()
                              
    def get_collect_icon_text(self):
        text = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_collect_icon_text_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_collect_icon_text')).text
        return text
    
    def get_course_title(self):
        title = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_course_title_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_course_title')).text
        
        return title
    
    def click_first_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_catalog_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_catalog_tab')).click()
                              
    def click_second_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_details_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_details_tab')).click()
                              
    def click_third_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_comment_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_comment_tab')).click()
    
    def click_four_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_related_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_related_tab')).click()
    
    
            
    def get_courseware_list(self):
        time.sleep(5)
        self.coursewarelist = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_courseware_list_by'), \
                             self.cfg.get('course_detail_page', 'course_detail_page_courseware_list'))
        coursewarelistitems = self.coursewarelist.find_elements_by_class_name(self.cfg.get('course_detail_page', 'course_detail_page_courseware_list_item'))
        return coursewarelistitems
    
    def get_courseware_list_length(self,list):
        listlen = len(list)
        return listlen
                                  
    def click_first_courseware_and_back_my_course(self,list,list_len):
        
        index = random.randint(1,list_len)
        list[index].click()
        
        time.sleep(15)
        
        self.dr.press_keycode(4)
        
    def click_customer_service_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_customer_service_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_customer_service_icon')).click()
        
    def click_download_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_download_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_download_icon')).click()
        
    
    def click_checkall_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_checkall_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_checkall_download')).click()
                              
    def click_start_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_start_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_start_download')).click()
          
    def click_cancel_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_cancel_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_cancel_download')).click()
