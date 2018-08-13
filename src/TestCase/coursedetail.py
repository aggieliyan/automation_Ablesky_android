# -*- coding: UTF-8 -*-
'''
Created on 2018-8-6

@author: ablesky
'''
import time
from PO.coursedetail_page import CourseDetailPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PO.schoolhome_page import SchoolHome
from PO.teacher_page import Teacher

import searchresult

def click_back_btn(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_back_btn()

def if_collect_course(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    collectedtext = coursedetail.get_collect_icon_text()
    if collectedtext == '收藏':
        return 1
    else:
        return 0

    
def click_collect_icon(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_collect_icon()



#�㲥��
def click_first_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_first_tab()

def click_second_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_second_tab()
 
def click_third_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_third_tab()

def click_four_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_four_tab()
   
def click_first_courseware(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    
    list = coursedetail.get_courseware_list()
    len = coursedetail.get_courseware_list_length(list)
    coursedetail.click_first_courseware_and_back_my_course(list,len)
    
def download_all_courseware(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    print u'点击下载'
    coursedetail.click_download_icon()
    print u'点击全选'
    coursedetail.click_checkall_download()
    print u'点击立即下载'
    coursedetail.click_start_download()
    element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'.//*[contains(@text,�����ء�)]')))
    return element    
    
def get_course_title(driver,cfg,coursetype):
    coursedetail = CourseDetailPage(driver,cfg)
    time.sleep(2)
    if "live" == coursetype:
        coursedetail.click_second_tab()
    else:
        coursedetail.click_first_tab()
    title = coursedetail.get_course_title()
    return title

def open_teacher_info(driver,cfg,index):
    coursedetail = CourseDetailPage(driver,cfg)
    teacherList = coursedetail.get_teacher_list()
    teacherName = coursedetail.get_teacher_name_list()[index].text
    print u"详情页老师：",teacherName
    print u"打开老师详情页"
    teacherList[index].click()
    teacher = Teacher(driver,cfg)
    driver.switch_to.context("WEBVIEW_com.ablesky.ui.activity")
    teacherAndOrgName = teacher.get_teacher_name()
    print u"老师详情页：",teacherAndOrgName
    #teacher.click_back_btn()
    if teacherName in teacherAndOrgName:
        return True
    else:
        return False
    
def open_org_info(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    orgname = coursedetail.get_org_name()
    coursedetail.click_org_info()
    school = SchoolHome(driver,cfg)
    driver.switch_to.context("WEBVIEW_com.ablesky.ui.activity")
    orgNameInSchoolHome = school.get_org_title()
    if orgname == orgNameInSchoolHome:
        return True
    else:
        return False
    
def open_course_tag(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    courseTag = coursedetail.get_course_tag_text()
    
    coursedetail.click_course_tag()
       
    key = searchresult.get_search_key(driver, cfg)
    
    searchresult.click_cancel_btn(driver, cfg)
    
    if(courseTag == key):
        return True
    else:
        return False

    
'''
#报班课程
def click_catalog_tab_class_page(driver, cfg):
    coursedetail = ClassCourseDetailPage(driver,cfg)
    coursedetail.click_catalog_tab()

def click_details_tab_class_page(driver, cfg):
    coursedetail = ClassCourseDetailPage(driver,cfg)
    coursedetail.click_details_tab()
 
def click_comment_tab_class_page(driver, cfg):
    coursedetail = ClassCourseDetailPage(driver,cfg)
    coursedetail.click_comment_tab()

def click_related_tab_class_page(driver, cfg):
    coursedetail = ClassCourseDetailPage(driver,cfg)
    coursedetail.click_related_tab()
    

#面授班课程
def click_classdetail_tab_face_page(driver, cfg):
    coursedetail = FaceCourseDetailPage(driver,cfg)
    coursedetail.click_classdetail_tab()

def click_details_tab_face_page(driver, cfg):
    coursedetail = FaceCourseDetailPage(driver,cfg)
    coursedetail.click_courseinfo_tab()
 
def click_related_tab_face_page(driver, cfg):
    coursedetail = FaceCourseDetailPage(driver,cfg)
    coursedetail.click_related_tab()
    

#ֱ直播课程
def click_courseware_tab_live_page(driver, cfg):
    coursedetail = LiveCourseDetailPage(driver,cfg)
    coursedetail.click_courseware_tab()

def click_details_tab_live_page(driver, cfg):
    coursedetail = LiveCourseDetailPage(driver,cfg)
    coursedetail.click_detail_tab()
'''