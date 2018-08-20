# -*- coding: UTF-8 -*-
'''
Created on 2018-8-17

@author: ablesky
'''
from PO.play_page import Play
import time

def click_back_btn(driver,cfg):
    playpage = Play(driver,cfg)
    playpage.click_back_btn()

def click_play_layout(driver,cfg):
    playpage = Play(driver,cfg)
    playpage.click_play_layout()
    
def play_video_and_exist(driver,cfg):
    time.sleep(15)
    playpage = Play(driver,cfg)
    
    playpage.click_play_layout()
    playpage.click_back_btn()