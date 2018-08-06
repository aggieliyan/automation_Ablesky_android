# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
from PO.mycourse_page import MyCourse
import time
import coursedetail
import examstart

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
    
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    mycourse.click_filter_btn()
    mycourse.choose_dianbo_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'dianbo')
        if title == playCourseTitle:
            coursedetail.click_back_btn(driver, cfg)
            return True
        else:
            return False
    else:
        return False


def click_my_course_page_presell_list_item(driver,cfg):
    
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    mycourse.click_filter_btn()
    mycourse.choose_presell_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'presell')
        if title == playCourseTitle:
            coursedetail.click_back_btn(driver, cfg)
            return True
        else:
            return False
    else:
        return False

def click_my_course_page_network_list_item(driver,cfg):
    
    mycourse = switch_to_dianbo_page(driver, cfg)
    time.sleep(2)
    mycourse.click_filter_btn()
    mycourse.choose_network_course()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    playCourseTitle = courselisttitles[0]
    
    if courselist:
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'network')
        if title == playCourseTitle:
            coursedetail.click_back_btn(driver, cfg)
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_live_list_item(driver,cfg):
    mycourse = switch_to_live_page(driver, cfg)
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    CourseTitle = courselisttitles[0]
    
    if courselist:
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'live')
        if title == CourseTitle:
            coursedetail.click_back_btn(driver, cfg)
            return True
        else:
            return False
    else:
        return False

def click_my_course_page_face_list_item(driver,cfg):
    mycourse = switch_to_faceCourse_page(driver, cfg)
    time.sleep(2)
    courselist = mycourse.get_course_list()
    courselisttitles = mycourse.get_course_list_titles()
    
    CourseTitle = courselisttitles[0]
    
    if courselist:
        mycourse.click_course_list_item(courselist,0)
        title = coursedetail.get_course_title(driver, cfg,'face')
        if title == CourseTitle:
            coursedetail.click_back_btn(driver, cfg)
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_examination_item(driver,cfg):
    mycourse = switch_to_exam_page(driver, cfg)
    mycourse.click_filter_btn()
    mycourse.choose_examination()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)

    examlist = mycourse.get_course_list()
    examlisttitles = mycourse.get_course_list_titles()
    
    examtitle = examlisttitles[0]
    
    if examlist:
        mycourse.click_course_list_item(examlist,0)
        title = examstart.get_exam_title(driver, cfg)
        examstart.click_back_btn(driver, cfg)
        if title == examtitle:            
            return True
        else:
            return False
    else:
        return False
    

def click_my_course_page_exercise_item(driver,cfg):
    mycourse = switch_to_exam_page(driver, cfg)
    mycourse.click_filter_btn()
    mycourse.choose_exercise()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)

    examlist = mycourse.get_course_list()
    examlisttitles = mycourse.get_course_list_titles()
    
    examtitle = examlisttitles[0]
    print 'examtitle:',examtitle
    
    if examlist:
        mycourse.click_course_list_item(examlist,0)
        title = examstart.get_exam_title(driver, cfg)
        print 'title:',title
        examstart.click_back_btn(driver, cfg)
        if title == examtitle:      
            return True
        else:
            return False
    else:
        return False


def click_my_course_page_question_bank_item(driver,cfg):
    mycourse = switch_to_exam_page(driver, cfg)
    mycourse.click_filter_btn()
    mycourse.choose_question()
    mycourse.click_filter_confirm_btn()
    time.sleep(2)
    
    questionlist = mycourse.get_course_list()
    if questionlist:
        mycourse.click_course_list_item(questionlist, 0)