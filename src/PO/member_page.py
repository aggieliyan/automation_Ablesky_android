# -*- coding: UTF-8 -*-
'''
Created on 2018-8-16

@author: ablesky
'''
from PO.base import Base

class Member(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        #ctxlist = self.dr.contexts
        #print "teacher ctx:",ctxlist
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('teacher_home_page', 'teacher_home_page_back_btn_by'), \
                             self.cfg.get('teacher_home_page', 'teacher_home_page_back_btn')).click()