# -*- coding: UTF-8 -*-
'''
Created on 2018-8-16

@author: ablesky
'''
from PO.base import Base

class Interest(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        #ctxlist = self.dr.contexts
        #print "teacher ctx:",ctxlist
        
    def get_page_title(self):
        title = self.dr.find_element(self.cfg.get('interest_page', 'interest_page_title_by'), \
                             self.cfg.get('interest_page', 'interest_page_title')).text
        return title
    
    def click_cancel_btn(self):
        self.dr.find_element(self.cfg.get('interest_page', 'interest_page_cancel_btn_by'), \
                             self.cfg.get('interest_page', 'interest_page_cancel_btn')).click()
                             
    
    def click_save_btn(self):
        self.dr.find_element(self.cfg.get('interest_page', 'interest_page_save_btn_by'), \
                             self.cfg.get('interest_page', 'interest_page_save_btn')).click()
                             
    def click_anoter_batch_btn(self):
        self.dr.find_element(self.cfg.get('interest_page', 'interest_page_another_batch_btn_by'), \
                             self.cfg.get('interest_page', 'interest_page_another_batch_btn')).click()
                             
    def get_interests(self):
        element = self.dr.find_element(self.cfg.get('interest_page', 'interest_page_interest_layout_by'), \
                             self.cfg.get('interest_page', 'interest_page_interest_layout'))
        element1 = element.find_element(self.cfg.get('interest_page', 'interest_page_interest_layout_list_by'), \
                             self.cfg.get('interest_page', 'interest_page_interest_layout_list'))
        interestsList = element1.find_elements(self.cfg.get('interest_page', 'interest_page_interest_layout_list_item_by'), \
                             self.cfg.get('interest_page', 'interest_page_interest_layout_list_item'))
        return interestsList
    
        
    