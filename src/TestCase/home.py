# -*- coding: UTF-8 -*-
'''
Created on 2018-8-3

@author: ablesky
'''

from PO.home_page import Home
from PO.base import Base

def close_the_suspended_advertisement(driver,cfg):
    homepage = Home(driver,cfg)
    homepage.click_the_suspended_advertisement_close_btn()

    
'''
关闭底部悬浮广告
'''
def close_the_suspended_advertisement_on_the_bottom(driver,cfg):     
    homepage = Home(driver,cfg)
    homepage.click_the_suspended_advertisement_close_btn()
   
'''
关闭评分对话框
'''    
def close_the_give_mark_dlg_by_click_cancel_btn(driver,cfg):
    homepage = Home(driver,cfg)
    homepage.click_the_give_mark_dlg_cancel_btn()
    
'''
关闭权限是否允许对话框
'''    
def allow_permission(driver,cfg):
    homepage = Home(driver,cfg)
    homepage.allow_permission()
    
def isHomePage(driver,cfg):
    base = Base(driver)
    base.switchToWebview()
    homepage = Home(driver,cfg)
    text = homepage.get_search_box_text()
    if u"搜索课程机构" == text:
        return True
    else:
        return False
    
def click_search_box(driver,cfg):
    homepage = Home(driver, cfg)
    base = Base(driver)
    base.switchToWebview()
    homepage.click_search_box()
    

    
'''
首次安装启动APP，引导页点击登录按钮进入登录页
'''
def click_startup_login_btn(driver,cfg):
    homepage = Home(driver, cfg)
    base = Base(driver)
    if homepage.get_startup_homepage() != None:
        base.swipLeft(500)
        base.swipLeft(500)
        homepage.click_startup_homepage_login_btn()
'''
首次安装启动APP，引导页点击跳过进入首页
'''    
def click_startup_skip_btn(driver,cfg):
    homepage = Home(driver, cfg)
    base = Base(driver)
    if homepage.get_startup_homepage() != None:
        base.swipLeft(500)
        base.swipLeft(500)
        homepage.click_startup_homepage_skip_btn() 


'''
启动APP，进入首页前是否需要关闭一些对话框或者页面
'''    
def enter_home_page(driver,cfg):
    try:
        print u'---是否有权限选择，若有点击允许，否则pass'
        allow_permission(driver, cfg)
    except:
        pass
    
    try:
        print u'---是否有启动页，若有点击立即体验，否则pass'
        click_startup_skip_btn(driver, cfg)
    except:
        pass
    
    try:        
        print u'---首页有广告关闭广告后进入个人中心,否则pass'
        close_the_suspended_advertisement(driver, cfg)
    except:
        pass
    
    try:
        print u"---若弹出评分对话框，关闭，否则pass"
        close_the_give_mark_dlg_by_click_cancel_btn(driver, cfg)
    except:
        pass
