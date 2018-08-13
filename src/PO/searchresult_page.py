# -*- coding: UTF-8 -*-
'''
Created on 2018-8-13

@author: ablesky
'''
from PO.base import Base

class SearchResult(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def click_cancel_btn(self):
        self.dr.find_element(self.cfg.get('search_result_page', 'search_result_page_cancel_btn_by'), \
                             self.cfg.get('search_result_page', 'search_result_page_cancel_btn')).click()
    
    def get_search_key_text(self):
        element = self.dr.find_element(self.cfg.get('search_result_page', 'search_result_page_search_key_by'), \
                             self.cfg.get('search_result_page', 'search_result_page_search_key'))
        return element.text
    
    def get_result_list(self):
        element = self.dr.find_element(self.cfg.get('search_result_page', 'search_result_page_result_list_by'), \
                             self.cfg.get('search_result_page', 'search_result_page_result_list'))
        return element
        
    def get_course_titles(self):
        elements = self.dr.find_elements(self.cfg.get('search_result_page', 'search_result_page_course_title_by'), \
                             self.cfg.get('search_result_page', 'search_result_page_course_title'))
        return elements                         
    