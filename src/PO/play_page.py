# -*- coding: UTF-8 -*-
'''
Created on 2018-8-17

@author: ablesky
'''
from PO.base import Base


class Play(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('play_page', 'play_page_back_btn_by'), \
                             self.cfg.get('play_page', 'play_page_back_btn')).click()
                             
    def click_play_layout(self):
        self.dr.find_element(self.cfg.get('play_page', 'play_page_play_layout_by'), \
                             self.cfg.get('play_page', 'play_page_play_layout')).click()
        
    def get_title(self):
        title = self.dr.find_element(self.cfg.get('play_page', 'play_page_title_by'), \
                             self.cfg.get('play_page', 'play_page_title')).text
        return title    