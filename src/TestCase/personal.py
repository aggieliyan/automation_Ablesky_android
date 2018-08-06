# -*- coding: UTF-8 -*-
'''
Created on 2018-8-3

@author: ablesky
'''

from PO.personal_page import Personal


def open_login_page_by_click_photo(driver,cfg):
    personalpage = Personal(driver,cfg)
    personalpage.click_unlogin_photo()
    
def open_login_page_by_click_login_or_register_text(driver,cfg):
    personalpage = Personal(driver,cfg)
    personalpage.click_login_or_register()
    