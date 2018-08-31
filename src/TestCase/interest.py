# -*- coding: UTF-8 -*-
'''
Created on 2018-8-16

@author: ablesky
'''
from PO.interest_page import Interest
import random
import time
from PO.setting_page import Setting

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def find_toast(driver,cfg,message):
    print 1111
    try:
        element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
        print "interestpage:",element.text
        return True
    except:
        print "except"
        return False

def click_cancel_btn(driver, cfg):
    interest = Interest(driver, cfg)
    interest.click_cancel_btn()
    
def click_save_btn(driver, cfg):
    interest = Interest(driver, cfg)
    interest.click_save_btn()
    
def click_anoter_batch_btn(driver, cfg):
    interest = Interest(driver, cfg)
    interest.click_anoter_batch_btn()

def get_title(driver, cfg):
    interest = Interest(driver, cfg)
    return interest.get_page_title()


#随机选择兴趣
def choose_interest(driver,cfg):
    interest = Interest(driver, cfg)
    list = interest.get_interests()
    length = len(list)
    index = random.randint(0,length-1)
    list[index].click()
    time.sleep(2)
    interest.click_anoter_batch_btn()
    list = interest.get_interests()
    length = len(list)
    index = random.randint(0,length-1)
    list[index].click()
    time.sleep(2)
    
    interest.click_save_btn()
    time.sleep(2)
    #setting = Setting(driver, cfg)
    #flag = setting.find_toast(u"保存成功!")
    #flag = find_toast(driver, cfg, u"保存成功!")
    #print flag
    #return flag
    