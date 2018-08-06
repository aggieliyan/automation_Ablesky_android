# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.base import Base


class ExamStartPage(Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg

    
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('exam_start_page', 'exam_start_page_back_btn_by'), \
                              self.cfg.get('exam_start_page', 'exam_start_page_back_btn')).click()
                              
    def click_start_btn(self):
        self.dr.find_element(self.cfg.get('exam_start_page', 'exam_start_page_start_btn_by'), \
                              self.cfg.get('exam_start_page', 'exam_start_page_start_btn')).click()
                              
    def get_exam_title(self):
        titles = self.dr.find_elements(self.cfg.get('exam_start_page', 'exam_start_page_title_by'), \
                              self.cfg.get('exam_start_page', 'exam_start_page_title'))
        return titles[1].text
    
    