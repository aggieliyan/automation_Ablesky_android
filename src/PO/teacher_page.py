# -*- coding: UTF-8 -*-
'''
Created on 2018-8-10

@author: ablesky
'''
from PO.base import Base

class Teacher(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        #ctxlist = self.dr.contexts
        #print "teacher ctx:",ctxlist
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('teacher_home_page', 'teacher_home_page_back_btn_by'), \
                             self.cfg.get('teacher_home_page', 'teacher_home_page_back_btn')).click()
        
    def get_page_title(self):
        ele = self.dr.find_element(self.cfg.get('teacher_home_page', 'teacher_home_page_title_by'), \
                             self.cfg.get('teacher_home_page', 'teacher_home_page_title'))
        return ele.text
    
    def get_teacher_name(self):
        ele = self.dr.find_element(self.cfg.get('teacher_home_page', 'teacher_home_page_teacher_name_by'), \
                             self.cfg.get('teacher_home_page', 'teacher_home_page_teacher_name'))
        return ele.text