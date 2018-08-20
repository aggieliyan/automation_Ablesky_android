# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.base import Base
import time


class MyCourse(Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        
    def click_back_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_back_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_back_btn')).click()
    
    def click_dianbo_course_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_dianbo_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_dianbo_btn')).click()
                           
    def click_live_course_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_live_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_live_btn')).click()
    
    def click_exam_course_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_exam_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_exam_btn')).click()
    
    def click_face_course_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_face_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_face_btn')).click()
    
    
    
    def click_search_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_search_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_search_btn')).click()
    
    def input_search_key(self,key):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_search_key_by'), \
                             self.cfg.get('my_course_page', 'my_course_search_key')).send_keys(key)
    
    def click_filter_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_filter_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_filter_btn')).click()
    
    def click_sort_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_sort_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_sort_btn')).click()
    
    def get_course_list(self):
        time.sleep(9)
        self.courselist = self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_list_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_list'))
        courselistitems = self.courselist.find_elements_by_class_name(self.cfg.get('my_course_page', 'my_course_page_list_item'))
        return courselistitems
                             
    def click_course_list_item(self,list,item):
        list[item].click()
        
    def get_course_list_titles(self):
        time.sleep(2)
        courselist = self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_list_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_list'))
        list = courselist.find_elements(self.cfg.get('my_course_page', 'my_course_page_listitem_title_by'), \
                                                                      self.cfg.get('my_course_page', 'my_course_page_listitem_title'))
        listtitles = []
        i = 0       
        while i < len(list):
            listtitles.append(list[i].text)
            i = i + 1
        
        return listtitles
        
    def choose_all_course(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_all_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_all')).click()
    
    
    def choose_dianbo_course(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_dianbo_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_dianbo')).click()
    
    def choose_presell_course(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_presell_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_presell')).click()
        
    def choose_network_course(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_network_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_course_type_network')).click()
    
    def choose_all_exam(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_all_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_all')).click()
    
                             
    def choose_examination(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_examination_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_examination')).click()
          
    def choose_exercise(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_exercise_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_exercise')).click()
    
    def choose_question(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_question_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_item_exam_type_question')).click()
        
    
    
    def click_filter_confirm_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_confirm_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_confirm_btn')).click()
        
    def click_filter_clear_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_filter_clear_btn_by'), \
                             self.cfg.get('my_course_page', 'my_course_page_filter_clear_btn')).click()
        
    def get_list_no_data_flag(self):
        time.sleep(2)
        noDataFlag = self.dr.find_element(self.cfg.get('my_course_page', 'my_course_page_no_data_by'), \
                              self.cfg.get('my_course_page', 'my_course_page_no_data')).text
        return noDataFlag