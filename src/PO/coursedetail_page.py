# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''

from PO.base import Base
import time
import random

class CourseDetailPage(Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg

    
    def click_back_btn(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_back_btn_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_back_btn')).click()
    
    
    def click_collect_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_collect_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_collect_icon')).click()
    
    
    def click_share_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_share_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_share_icon')).click()
                              
    def get_collect_icon_text(self):
        text = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_collect_icon_text_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_collect_icon_text')).text
        return text
    
    def get_course_title(self):
        title = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_course_title_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_course_title')).text
        
        return title
    
    def click_first_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_catalog_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_catalog_tab')).click()
                              
    def click_second_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_details_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_details_tab')).click()
                              
    def click_third_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_comment_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_comment_tab')).click()
    
    def click_four_tab(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_related_tab_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_page_related_tab')).click()
    
    
            
    def get_courseware_list(self):
        time.sleep(2)
        coursewarelist = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_page_courseware_list_by'), \
                             self.cfg.get('course_detail_page', 'course_detail_page_courseware_list'))
        coursewarelistitems = coursewarelist.find_elements(self.cfg.get('course_detail_page', 'course_detail_page_courseware_list_item_by'), \
                                                           self.cfg.get('course_detail_page', 'course_detail_page_courseware_list_item'))
        return coursewarelistitems
    
    def get_courseware_titles(self):
        coursewaretitles = self.dr.find_elements(self.cfg.get('course_detail_page', 'course_detail_content_title_by'), \
                             self.cfg.get('course_detail_page', 'course_detail_content_title'))
        return coursewaretitles
    
    def get_courseware_list_length(self,list):
        listlen = len(list)
        return listlen
                                  
    def play_courseware_and_back_my_course(self,list,list_len):
        
        index = random.randint(0,list_len-1)
        list[index].click()
        
    def click_video_box(self):
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_video_box_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_video_box')).click()
        
    def click_full_screen_btn(self):
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_fullscreen_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_fullscreen')).click()
           
    def click_video_box_back_btn(self):
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_video_box_back_btn_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_video_box_back_btn')).click()
           
    
    def click_customer_service_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_customer_service_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_customer_service_icon')).click()
        
    def click_download_icon(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_download_icon_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_download_icon')).click()
        
    
    def click_checkall_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_checkall_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_checkall_download')).click()
                              
    def click_start_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_start_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_start_download')).click()
          
    def click_cancel_download(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_cancel_download_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_cancel_download')).click()

    def click_org_info(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_org_layout_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_org_layout')).click()
    
    def get_org_follow_text(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_org_follow_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_org_follow'))
        return element.text
    
    def click_org_follow(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_org_follow_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_org_follow')).click()
    
    def get_course_tag_text(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_tag_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_tag'))
        return element.text
    
    def click_course_tag(self):
        time.sleep(2)
        self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_tag_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_tag')).click()
    
    def get_teacher_list(self):
        time.sleep(2)
        teachersElement = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_teachers_layout_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_teachers_layout'))
        teacherslist = teachersElement.find_elements(self.cfg.get('course_detail_page', 'course_detail_teachers_layout_item_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_teachers_layout_item'))
        return teacherslist
    
    def get_teacher_name_list(self):
        time.sleep(2)
        teacherNameList = self.dr.find_elements(self.cfg.get('course_detail_page', 'course_detail_teacher_name_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_teacher_name'))
        return teacherNameList
    
    def get_org_name(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_org_name_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_org_name'))
        return element.text
    
    def get_bottom_recommend_list(self):
        time.sleep(2)
        list = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list'))
        recommendList = list.find_elements(self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list_item_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list_item'))
        return recommendList
    
    def get_bottom_recommend_list_item_title(self):
        time.sleep(2)
        titlesList = self.dr.find_elements(self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list_item_title_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_bottom_recommend_list_item_title'))
        return titlesList
    
    def click_page_first_hint_vew(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_first_hint_view_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_first_hint_view'))
        element.click()
    
    
    def click_play_first_hint_vew(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_play_first_hint_view_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_play_first_hint_view'))
        element.click()
    
    
    def click_play_second_hint_vew(self):
        time.sleep(2)
        element = self.dr.find_element(self.cfg.get('course_detail_page', 'course_detail_play_second_hint_view_by'), \
                              self.cfg.get('course_detail_page', 'course_detail_play_second_hint_view'))
        element.click()
    