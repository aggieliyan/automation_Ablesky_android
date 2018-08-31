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

from PO.base import Base

import searchresult

'''
点击返回按钮
'''
def click_back_btn(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_back_btn()

'''
点击中屏播放时的返回按钮
'''
def click_video_box_back_btn(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_video_box_back_btn()

'''
判断该课程是否收藏，已收藏返回True，未收藏返回False
'''
def if_collect_course(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    collectedtext = coursedetail.get_collect_icon_text()
    if '收藏' == collectedtext:
        return False
    else:
        return True

'''
点击收藏按钮
'''    
def click_collect_icon(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_collect_icon()

'''
切换到详情tab
''' 
def click_first_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_first_tab()

'''
切换到目录tab
'''
def click_second_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_second_tab()

'''
切换到提问tab
''' 
def click_third_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_third_tab()

'''
切换到相关tab
'''
def click_four_tab(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_four_tab()
   
def click_first_courseware(driver, cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    
    #获取课件列表
    list = coursedetail.get_courseware_list()
    #获取列表长度
    len = coursedetail.get_courseware_list_length(list)
    coursedetail.click_first_courseware_and_back_my_course(list,len)
    
def download_all_courseware(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    print u'---点击下载'
    coursedetail.click_download_icon()
    print u'---点击全选'
    coursedetail.click_checkall_download()
    print u'---点击立即下载'
    coursedetail.click_start_download()
    
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
    print u"---打开老师详情页"
    teacherList[index].click()
    teacher = Teacher(driver,cfg)
    base = Base(driver)
    #切换到webview模式，否则不能对wap页的元素进行操作
    base.switchToWebview()
    teacherAndOrgName = teacher.get_teacher_name()
    #teacher.click_back_btn()
    if teacherName in teacherAndOrgName:
        return True
    else:
        return False
    
def open_org_info(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    orgname = coursedetail.get_org_name()
    print u"---点击机构信息进入机构首页"
    coursedetail.click_org_info()
    school = SchoolHome(driver,cfg)
    base = Base(driver)
    #切换到webview模式，否则不能对wap页的元素进行操作
    base.switchToWebview()
    orgNameInSchoolHome = school.get_org_title()
    if orgname == orgNameInSchoolHome:
        return True
    else:
        return False
    
def open_course_tag(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    courseTag = coursedetail.get_course_tag_text()
    print u"---点击课程标签"
    coursedetail.click_course_tag()
    time.sleep(3)
    key = searchresult.get_search_key(driver, cfg)
    
    searchresult.click_cancel_btn(driver, cfg)
    
    if(courseTag == key):
        return True
    else:
        return False
    
def click_bottom_recommend_course(driver,cfg,item):
    coursedetail = CourseDetailPage(driver,cfg)
    #获取底部推荐课程列表
    courseList = coursedetail.get_bottom_recommend_list()
    title = coursedetail.get_bottom_recommend_list_item_title()[item].text
    #有的课程名称较长，显示名称...，所以校验名称是否一致时需要去掉...
    if '...' in title:
        title = title[:-3]
    print u"---点击第",item+1,u"个推荐课程"
    courseList[item].click()
    time.sleep(3)
    currentTitle = get_course_title(driver,cfg,"dianbo")
    if(title in currentTitle):
        return True
    else:
        return False
    
def click_video_box(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_video_box()
    
def play_courseware(driver,cfg,index):
    coursedetail = CourseDetailPage(driver,cfg)
    #获取课件列表
    coursewarelist = coursedetail.get_courseware_list()
    print u"---点击课件播放"
    coursewarelist[index].click()
    
    '''
          通过id定位不到引导页，所以先这样做，以后又更好方法再修改
    '''
    #获取手机屏幕分辨率
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    #关闭播放引导页
    driver.tap([(x/4,y/6)],200)
    driver.tap([(x/4,y/6)],200)
    '''
    try:
        print u"---若有播放引导页，关闭，而且pass"
        coursedetail.close_play_hint_view(driver,cfg)
    except:
        print 'no found hint view,pass'
        pass
    '''
    time.sleep(10)
    #点击中屏播放器，唤出大屏按钮等
    click_video_box(driver,cfg)
    #driver.tap([(0,0),(1080,607)],500)
    print u"---全屏播放"
    coursedetail.click_full_screen_btn()
    
def close_page_hint_view(driver,cfg):
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_page_first_hint_vew()
    
def close_play_hint_view(driver,cfg):
    print 11111111111111111
    coursedetail = CourseDetailPage(driver,cfg)
    coursedetail.click_play_first_hint_vew()
    time.sleep(1)
    coursedetail.click_play_second_hint_vew()
    
    
    
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