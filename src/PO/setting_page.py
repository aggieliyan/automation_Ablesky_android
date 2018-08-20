# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.base import Base

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Setting(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def find_toast(self,message):
        try:
            element = WebDriverWait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
            print "settingpage:",element.text
            return True
        except:
            return False
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('setting_page', 'setting_page_back_btn_by'), \
                             self.cfg.get('setting_page', 'setting_page_back_btn')).click()
                             
    def click_logout_btn(self):
        self.dr.find_element(self.cfg.get('setting_page', 'setting_page_logout_btn_by'), \
                             self.cfg.get('setting_page', 'setting_page_logout_btn')).click()
                             
    def click_set_interest_item(self):
        self.dr.find_element(self.cfg.get('setting_page', 'setting_page_set_interest_by'), \
                             self.cfg.get('setting_page', 'setting_page_set_interest')).click()