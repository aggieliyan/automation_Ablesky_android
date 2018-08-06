# -*- coding: UTF-8 -*-

from PO.base import Base
import time

class Index(Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        
    def click_tab_home_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('index_page', 'tab_home_btn_by'), \
                              self.cfg.get('index_page', 'tab_home_btn')).click()
                              
    def click_tab_circle_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('index_page', 'tab_able_circle_btn_by'), \
                              self.cfg.get('index_page', 'tab_able_circle_btn')).click()
                              
    def click_tab_vip_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('index_page', 'tab_vip_btn_by'), \
                              self.cfg.get('index_page', 'tab_vip_btn')).click()
                              
    def click_tab_communicate_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('index_page', 'tab_communicate_btn_by'), \
                              self.cfg.get('index_page', 'tab_communicate_btn')).click()
                              
    def click_tab_myself_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('index_page', 'tab_myself_btn_by'), \
                              self.cfg.get('index_page', 'tab_myself_btn')).click()
                            