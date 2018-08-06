# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.examstart_page import ExamStartPage

def click_back_btn(driver,cfg):
    examstart = ExamStartPage(driver,cfg)
    examstart.click_back_btn()
    
def click_start_btn(driver,cfg):
    examstart = ExamStartPage(driver,cfg)
    examstart.click_start_btn()

def get_exam_title(driver,cfg):
    examstart = ExamStartPage(driver,cfg)
    title = examstart.get_exam_title()
    return title