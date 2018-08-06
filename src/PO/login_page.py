# -*- coding: UTF-8 -*-

from PO.base import Base
import time


class Login(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('login_page', 'login_back_by'), \
                             self.cfg.get('login_page', 'login_back')).click()
    
    def get_page_title(self):
        element = self.dr.find_element(self.cfg.get('login_page', 'login_page_title_by'), \
                             self.cfg.get('login_page', 'login_page_title'))
        return element.text

    def input_username(self, user_name):                   
        self.username = self.dr.find_element(self.cfg.get('login_page', 'login_username_by'), \
                             self.cfg.get('login_page', 'login_username'))
        self.username.send_keys(user_name)

    def input_pwd(self, user_pwd):
        self.password = self.dr.find_element(self.cfg.get('login_page', 'login_pwd_by'), \
                             self.cfg.get('login_page', 'login_pwd'))
        self.password.send_keys(user_pwd)

    def click_login_btn(self):
        self.loginbtn = self.dr.find_element(self.cfg.get('login_page', 'login_btn_by'), \
                             self.cfg.get('login_page', 'login_btn'))
        self.loginbtn.click()
                                                        
    
    
    
