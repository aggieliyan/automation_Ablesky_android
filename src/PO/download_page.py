# -*- coding: UTF-8 -*-
'''
Created on 2018-8-21

@author: ablesky
'''
from PO.base import Base

class DownloadPage(Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        
    def click_back_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_back_btn_by'), \
                              self.cfg.get('download_page', 'download_back_btn')).click()
                              
    def click_switch_layout_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_switch_layout_by'), \
                              self.cfg.get('download_page', 'download_switch_layout')).click()
                              
    def click_edit_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_edit_and_cancel_btn_by'), \
                              self.cfg.get('download_page', 'download_edit_and_cancel_btn')).click()
    
    def click_cancel_edit_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_edit_and_cancel_btn_by'), \
                              self.cfg.get('download_page', 'download_edit_and_cancel_btn')).click()
    
    def click_selete_all_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_selete_all_btn_by'), \
                              self.cfg.get('download_page', 'download_selete_all_btn')).click()
      
    def click_delete_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_delete_btn_by'), \
                              self.cfg.get('download_page', 'download_delete_btn')).click()
    
    def click_delete_cancel_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_cancel_deleted_courseware_btn_by'), \
                              self.cfg.get('download_page', 'download_cancel_deleted_courseware_btn')).click()
    
    def click_delete_sure_btn(self):
        self.dr.find_element(self.cfg.get('download_page', 'download_sure_deleted_courseware_btn_by'), \
                              self.cfg.get('download_page', 'download_sure_deleted_courseware_btn')).click()
    
        
    def get_download_list(self):
        list = self.dr.find_element(self.cfg.get('download_page', 'download_list_by'), \
                              self.cfg.get('download_page', 'download_list'))
        downloadcourselistitems = list.find_elements(self.cfg.get('download_page', 'download_list_item_by'), \
                                                     self.cfg.get('download_page', 'download_list_item'))
        return downloadcourselistitems
    
        
    def get_all_download_course_title_list(self):
        list = self.dr.find_elements(self.cfg.get('download_page', 'download_course_title_by'), \
                              self.cfg.get('download_page', 'download_course_title'))
        downloadlisttitles = []
        i = 0       
        while i < len(list):
            downloadlisttitles.append(list[i].text)
            i = i + 1
        
        return downloadlisttitles
    
    
    def get_all_download_courseware_current_speed_list(self):
        list = self.dr.find_elements(self.cfg.get('download_page', 'download_current_speed_by'), \
                              self.cfg.get('download_page', 'download_current_speed'))
        
        currentspeedlist = []
        i = 0       
        while i < len(list):
            currentspeedlist.append(list[i].text)
            i = i + 1
        
        return currentspeedlist
    
    
    def get_download_courseware_list(self):
        list = self.dr.find_elements(self.cfg.get('download_page', 'download_current_speed_by'), \
                              self.cfg.get('download_page', 'download_current_speed'))
        return list
    