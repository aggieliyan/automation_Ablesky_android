# -*- coding: UTF-8 -*-


from PO.login_page import Login
import time
import home
from PO.index_page import Index
import personal
from PO.personal_page import Personal
from PO.setting_page import Setting

def click_back_btn(driver,cfg):
    loginpage = Login(driver, cfg)
    loginpage.click_back_btn()

def get_login_page_title(driver,cfg):
    loginpage = Login(driver, cfg)
    title = loginpage.get_page_title()
    return title

def open_login_page(driver,cfg):
    print u'首页有广告关闭广告后进入个人中心,否则pass'
    try:
        home.close_the_suspended_advertisement(driver, cfg)
    except:
        pass
    index = Index(driver,cfg)
    index.click_tab_myself_btn()
    print u'点击登录/注册进入登录页面'
    personal.open_login_page_by_click_login_or_register_text(driver, cfg)
    

# 使用手机号登录
def login_by_mobile(cfg, driver, mobile_num, mobile_pwd):
    open_login_page(driver,cfg)
    loginpage = Login(driver, cfg)
    loginpage.input_username(mobile_num)
    loginpage.input_pwd(mobile_pwd)
    driver.press_keycode(4)
    time.sleep(2)
    
    loginpage.click_login_btn()
    time.sleep(2)

# 使用用户名登录  
def login_by_username(cfg, driver, username_num, username_pwd):
    open_login_page(driver,cfg)
    loginpage = Login(driver, cfg)
    loginpage.input_username(username_num)
    loginpage.input_pwd(username_pwd)  
    driver.press_keycode(4)
    time.sleep(2)
    loginpage.click_login_btn()
    print u'登录成功'
    time.sleep(2)
    
# 使用邮箱登录
def login_by_email(cfg, driver, email_num, email_pwd):
    open_login_page(driver,cfg)
    loginpage = Login(driver, cfg)
    loginpage.input_username(email_num)
    loginpage.input_pwd(email_pwd)
    driver.press_keycode(4)
    time.sleep(2)
    loginpage.click_login_btn()
    time.sleep(2)
    
def logout_by_exit_btn(driver,cfg):
    personal.open_setting_page(driver, cfg)
    
    settingpage = Setting(driver, cfg)
    settingpage.click_logout_btn()
    
    

