# -*- coding: UTF-8 -*-
'''
Created on 2018-8-3

@author: ablesky
'''

from PO.home_page import Home

def close_the_suspended_advertisement(driver,cfg):
    homepage = Home(driver,cfg)
    homepage.click_the_suspended_advertisement_close_btn()


def close_the_suspended_advertisement_on_the_bottom(driver,cfg):     
    homepage = Home(driver,cfg)
    homepage.click_the_suspended_advertisement_close_btn()
