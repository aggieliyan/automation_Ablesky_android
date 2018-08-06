# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.base import Base

class Setting(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('setting_page', 'setting_page_back_btn_by'), \
                             self.cfg.get('setting_page', 'setting_page_back_btn')).click()
                             
    def click_logout_btn(self):
        self.dr.find_element(self.cfg.get('setting_page', 'setting_page_logout_btn_by'), \
                             self.cfg.get('setting_page', 'setting_page_logout_btn')).click()