# -*- coding: UTF-8 -*-

from PO.base import Base
import time


class Personal(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver

    def click_unlogin_photo(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_unlogin_photo_by'), \
                             self.cfg.get('personal_page', 'personal_page_unlogin_photo')).click()
                                                        
    def click_login_or_register(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_login_or_register_by'), \
                             self.cfg.get('personal_page', 'personal_page_login_or_register')).click()
    
    def click_setting(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_setting_btn_by'), \
                             self.cfg.get('personal_page', 'personal_page_setting_btn')).click()
    
    
