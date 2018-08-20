# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.mycourse_page import MyCourse
import time
import coursedetail
import examstart
import os

set_baidu_ime = "adb shell ime set com.baidu.input_bbk.service/.PinyinIME"
def input_method_appium(ime):
    os.system(ime)

def search_course_and_open_the_course_detail(driver,cfg):
    mycourse = MyCourse(driver, cfg)
    '''mycourse.click_search_btn()
    print u"---切换输入法"
    try:
        input_method_appium(set_baidu_ime)
    except Exception,e:
        print e
    mycourse.input_search_key(key)
    #KEYCODE_ENTER--回车键---66
    driver.press_keycode(66)
    '''
    '''
    mycourse.click_search_btn()
    mycourse.input_search_key("pdf")
    #KEYCODE_ENTER--回车键---66
    driver.press_keycode(83)
    '''
    
    courselist = mycourse.get_course_list()
    print u"---打开课程详情页"
    mycourse.click_course_list_item(courselist,0)
    

def click_back_btn(driver,cfg):
    time.sleep(2)
    mycourse = MyCourse(driver,cfg)
    mycourse.click_back_btn()
    
def switch_to_dianbo_page(driver,cfg):
    mycourse = MyCourse(driver,cfg)
    mycourse.click_dianbo_course_btn()
    return mycourse

def switch_to_live_page(driver,cfg):
    mycourse = MyCourse(driver,cfg)
    mycourse.click_live_course_btn()
    return mycourse
    
def switch_to_exam_page(driver,cfg):
    mycourse = MyCourse(driver,cfg)
    mycourse.click_exam_course_btn()
    return mycourse
    
def switch_to_faceCourse_page(driver,cfg):
    mycourse = MyCourse(driver,cfg)
    mycourse.click_face_course_btn()
    return mycourse

def open_dianbo_course_detail(driver,cfg):
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    mycourse.click_filter_btn()
    mycourse.choose_dianbo_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    
    try:
        mycourse.click_course_list_item(courselist,0)
    except Exception,e:
        print e
        
    
def click_my_course_page_dianbo_list_item(driver,cfg):
    print u"---切换到点播"
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    print u"---选择点播课"
    mycourse.click_filter_btn()
    mycourse.choose_dianbo_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        print u"---打开点播课详情页"
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'dianbo')
        if title == playCourseTitle:
            return True
        else:
            return False
    else:
        return False


def click_my_course_page_presell_list_item(driver,cfg):
    print u"---切换到点播"
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    print u"---选择预售班课程"
    mycourse.click_filter_btn()
    mycourse.choose_presell_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        print u"---打开预售班详情页"
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'presell')
        if title == playCourseTitle:
            return True
        else:
            return False
    else:
        return False

def click_my_course_page_network_list_item(driver,cfg):
    print u"---切换到点播"
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    print u"---选择网络班课程"
    mycourse.click_filter_btn()
    mycourse.choose_network_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        print u"---打开网络班详情页"
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'network')
        if title == playCourseTitle:
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_live_list_item(driver,cfg):
    print u"---切换到直播"
    mycourse = switch_to_live_page(driver, cfg)
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    CourseTitle = courselisttitles[0]
    
    if courselist:
        print u"---打开直播课详情页"
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'live')
        if title == CourseTitle:
            return True
        else:
            return False
    else:
        return False

def click_my_course_page_face_list_item(driver,cfg):
    print u"---切换到面授班"
    mycourse = switch_to_faceCourse_page(driver, cfg)
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    CourseTitle = courselisttitles[0]
    
    if courselist:
        print u"---打开面授班课程详情页"
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'face')
        if title == CourseTitle:
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_examination_item(driver,cfg):
    print u"---切换到考试练习"
    mycourse = switch_to_exam_page(driver, cfg)
    print u"---选择考试卷"
    mycourse.click_filter_btn()
    mycourse.choose_examination()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)

    examlist = mycourse.get_course_list()
    examlisttitles = mycourse.get_course_list_titles()
    
    examtitle = examlisttitles[0]
    
    if examlist:
        print u"---打开考试卷开始答题页"
        mycourse.click_course_list_item(examlist,0)
        title = examstart.get_exam_title(driver, cfg)
        if title == examtitle:            
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_exercise_item(driver,cfg):
    print u"---切换到考试练习"
    mycourse = switch_to_exam_page(driver, cfg)
    print u"---选择练习卷"
    mycourse.click_filter_btn()
    mycourse.choose_exercise()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)

    examlist = mycourse.get_course_list()
    examlisttitles = mycourse.get_course_list_titles()
    
    examtitle = examlisttitles[0]
    
    if examlist:
        print u"---打开练习卷开始答题页"
        mycourse.click_course_list_item(examlist,0)
        title = examstart.get_exam_title(driver, cfg)
        if title == examtitle:      
            return True
        else:
            return False
    else:
        return False


def click_my_course_page_question_bank_item(driver,cfg):
    print u"---切换到考试练习"
    mycourse = switch_to_exam_page(driver, cfg)
    print u"---选择题库"
    mycourse.click_filter_btn()
    mycourse.choose_question()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    
    questionlist = mycourse.get_course_list()
    if questionlist:
        print u"---打开题库开始答题页面"
        mycourse.click_course_list_item(questionlist, 1)
        title = examstart.get_question_bank_title(driver, cfg)
        if u"题库详情" == title:      
            return True
        else:
            return False
    else:
        return False