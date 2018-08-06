# -*- coding: UTF-8 -*-
'''
Created on 2018-8-3

@author: ablesky
'''

from PO.base import Base

class Home(Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        
    
    #关闭首页悬浮广告  
    def click_the_suspended_advertisement_close_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_ads_close_btn_by'), \
                              self.cfg.get('home_page', 'home_page_ads_close_btn'))
        element.click()
        
    #关闭首页悬浮底部广告  
    def click_the_suspended_advertisement_bottom_close_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_ads_close_bottom_btn_by'), \
                              self.cfg.get('home_page', 'home_page_ads_close_bottom_btn'))
        element.click()
