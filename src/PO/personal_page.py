# -*- coding: UTF-8 -*-

from PO.base import Base


class Personal(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        
    def get_username_text(self):
        username = self.dr.find_element(self.cfg.get('personal_page', 'personal_page_username_by'), \
                             self.cfg.get('personal_page', 'personal_page_username')).text
        return username    
    #未登录状态点击下头像
    def click_unlogin_photo(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_unlogin_photo_by'), \
                             self.cfg.get('personal_page', 'personal_page_unlogin_photo')).click()
    #未登录状态下点击登录/注册                                                   
    def click_login_or_register(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_login_or_register_by'), \
                             self.cfg.get('personal_page', 'personal_page_login_or_register')).click()
    #点击设置
    def click_setting(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_setting_btn_by'), \
                             self.cfg.get('personal_page', 'personal_page_setting_btn')).click()
    #点击搜索
    def click_search(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_search_btn_by'), \
                             self.cfg.get('personal_page', 'personal_page_search_btn')).click()
    #点击会员广告
    def click_vip_nologin_ads(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_vip_nologin_by'), \
                             self.cfg.get('personal_page', 'personal_page_vip_nologin')).click()
    #点击我的课程
    def click_my_course(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_course_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_course')).click()
    #点击我的收藏
    def click_my_collect(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_collect_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_collect')).click()
    #点击关注网校
    def click_pay_attention_school(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_pay_attention_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_pay_attention')).click()
    #点击我的下载
    def click_my_download(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_download_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_download')).click()
    #点击优惠券
    def click_my_coupon(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_coupon_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_coupon')).click()
    #点击会员
    def click_my_vip(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_vip_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_vip')).click()
    #点击账户余额
    def click_balance(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_balance_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_balance')).click()
    #点击推荐有奖
    def click_award(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_award_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_award')).click()
    #点击分享收益
    def click_share_earning(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_my_share_earning_by'), \
                             self.cfg.get('personal_page', 'personal_page_my_share_earning')).click() 
    #点击学习记录的更多按钮
    def click_studyhistory_more_btn(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_studyHistory_more_by '), \
                             self.cfg.get('personal_page', 'personal_page_studyHistory_more')).click()
    #点击今日热学的更多按钮
    def click_todayhot_more_btn(self):
        self.dr.find_element(self.cfg.get('personal_page', 'personal_page_todayhot_more_by'), \
                             self.cfg.get('personal_page', 'personal_page_todayhot_more')).click()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
