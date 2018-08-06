# -*- coding: UTF-8 -*-

from PO.base import Base
import time


class Login(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver

    def input_username(self, user_name):
        time.sleep(2)
                           
        self.username = self.dr.find_element(self.cfg.get('login_page', 'login_username_by'), \
                             self.cfg.get('login_page', 'login_username'))
        self.username.send_keys(user_name)

    def input_pwd(self, user_pwd):
        time.sleep(2)
        self.password = self.dr.find_element(self.cfg.get('login_page', 'login_pwd_by'), \
                             self.cfg.get('login_page', 'login_pwd'))
        self.password.send_keys(user_pwd)

    def click_login_btn(self):
        time.sleep(2)
        self.loginbtn = self.dr.find_element(self.cfg.get('login_page', 'login_btn_by'), \
                             self.cfg.get('login_page', 'login_btn'))
        self.loginbtn.click()
        time.sleep(2)
                                                        
    
    
    
