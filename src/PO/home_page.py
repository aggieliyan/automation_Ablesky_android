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
        
    def get_search_box_text(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_search_box_by'), \
                              self.cfg.get('home_page', 'home_page_search_box'))
        return element.text
    
    def click_search_box(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_search_box_by'), \
                              self.cfg.get('home_page', 'home_page_search_box'))
        element.click()
        
    def click_the_give_mark_dlg_sure_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_give_mark_sure_btn_by'), \
                              self.cfg.get('home_page', 'home_page_give_mark_sure_btn'))
        element.click()
    
    def click_the_give_mark_dlg_cancel_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_give_mark_cancel_btn_by'), \
                              self.cfg.get('home_page', 'home_page_give_mark_cancel_btn'))
        element.click()
        
    def get_startup_homepage(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_startup_by'), \
                              self.cfg.get('home_page', 'home_page_startup'))
        return element
    
    def click_startup_homepage_login_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_startup_login_by'), \
                              self.cfg.get('home_page', 'home_page_startup_login'))
        element.click()
    
    def click_startup_homepage_skip_btn(self):
        element = self.dr.find_element(self.cfg.get('home_page', 'home_page_startup_skip_by'), \
                              self.cfg.get('home_page', 'home_page_startup_skip'))
        element.click()
