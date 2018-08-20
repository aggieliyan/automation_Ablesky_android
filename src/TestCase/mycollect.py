# -*- coding: UTF-8 -*-
'''
Created on 2018-8-15

@author: ablesky
'''
from PO.mycollect_page import MyCollectPage
import time
import coursedetail

def click_back_btn(driver, cfg):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    mycollect.click_back_btn()

 
def click_sure_btn_after_open_clear_dlg(driver, cfg):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    try:
        collectcourselist = mycollect.get_collectcourse_list()
        list_len = mycollect.get_collectcourse_list_length(collectcourselist)
        if list_len != 0:
            print u"---点击清空按钮"
            mycollect.click_clear_btn()
            print u"---确定清空"
            mycollect.click_clear_dlg_sure_btn()
    
        noDataFlag = mycollect.get_list_no_data_flag()
        return noDataFlag
    except:
        print u"---我的收藏页面为空，NoSuchElementException"
        return False
    
    
    
    
def click_cancel_btn_after_open_clear_dlg(driver, cfg):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    try:
        collectcourselist = mycollect.get_collectcourse_list()
        list_len = mycollect.get_collectcourse_list_length(collectcourselist)
        if list_len != 0:
            print u"---点击清空按钮"
            mycollect.click_clear_btn()
            print u"---取消清空"
            mycollect.click_clear_dlg_cancel_btn()
    
        list_len = mycollect.get_collectcourse_list_length(mycollect.get_collectcourse_list())
        if list_len != 0:
            return True
        else:
            return False
    except:
        print u"---我的收藏页面为空，NoSuchElementException"
        return False
    
   
    
def click_collect_list_item_to_open_course_detail(driver, cfg,index):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    try:
        collectcourselist = mycollect.get_collectcourse_list()
        list_len = mycollect.get_collectcourse_list_length(collectcourselist)
        if list_len:
            mycollect.click_collectcourseitem(collectcourselist, index)
            time.sleep(5)
    except:
        print u"---我的收藏列表为空，NoSuchElementException" 
        
    

def open_course_detail_which_course_click_collect_icon(driver, cfg, coursetitle):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    collectcourselist = mycollect.get_collectcourse_list()
    list_len = mycollect.get_collectcourse_list_length(collectcourselist)
    
    collecttitlelist = mycollect.get_list_titles()
    
    item = 0
    i = 0
    while i < list_len:
        if(coursetitle == collecttitlelist[i]):
            item = i
            break
        i = i + 1
    
    if list_len:
        mycollect.click_collectcourseitem(collectcourselist, item)
        return 1
    else:
        return 0

#长按取消收藏课程
def abolish_the_course_of_collection_by_longclick(driver,cfg,index):
    time.sleep(2)
    mycollect = MyCollectPage(driver,cfg)
    
    try:
        collecttitlelist = mycollect.get_list_titles()
        theFirstCourseTitle = collecttitlelist[0]
    
        courseList = mycollect.get_collectcourse_list()
        listLength = mycollect.get_collectcourse_list_length(courseList)
        if 0 != listLength:
            print u"---长按课程"
            mycollect.longClick_collectcourseitem(courseList, index)
            print u"---点击确定，取消收藏"
            mycollect.click_cancel_abolish_dlg_sure_btn()
        
            if 0 != (listLength -1):
                newCollectTitleList = mycollect.get_list_titles()
                newFirstCourseTitle = newCollectTitleList[index]
    
                if newFirstCourseTitle != theFirstCourseTitle:
                    return 1
                else:
                    return 0
            else:
                noDataFlag = mycollect.get_list_no_data_flag()
                if u"暂时没有收藏" == noDataFlag:
                    return 1
                else:
                    return 0
        else:   
            return u"暂时没有收藏不能取消收藏"
    except:
        print u"---我的收藏页面为空，NoSuchElementException"
        return 0
        
    
    
#取消收藏第一个课程      
def abolish_the_course_of_collection_in_coursedetail(driver,cfg,index):
    time.sleep(2)
    mycollect = MyCollectPage(driver, cfg)
    try:
        collecttitlelist = mycollect.get_list_titles()
        title = collecttitlelist[index]
        if len(collecttitlelist):
            print u"---打开第",index+1,u"个课程详情页"
            click_collect_list_item_to_open_course_detail(driver, cfg,index)
            time.sleep(2)
            print u"---取消收藏该课程"
            coursedetail.click_collect_icon(driver, cfg)
            print u"---返回我的收藏页面"
            coursedetail.click_back_btn(driver, cfg)
            
        
            if 0 != (len(collecttitlelist) -1):
                newCollectTitleList = mycollect.get_list_titles()
                newFirstCourseTitle = newCollectTitleList[index]
    
                if newFirstCourseTitle != title:
                    return 1
                else:
                    return 0
            else:
                noDataFlag = mycollect.get_list_no_data_flag()
                if u"暂时没有收藏" == noDataFlag:
                    return 1
                else:
                    return 0
        else:
            return u"暂时没有收藏不能取消收藏"
    except:
        print u"---我的收藏页面为空，NoSuchElementException"
        return 0
    '''
    print u"---打开第",index+1,u"个课程详情页"
    ifopencoursedetail = click_collect_list_item_to_open_course_detail(driver, cfg,index)
        
    if ifopencoursedetail:
        ifcollected = coursedetail.if_collect_course(driver, cfg)
        if ifcollected:
            time.sleep(2)
            print u"---取消收藏该课程"
            coursedetail.click_collect_icon(driver, cfg)
            ifcollected = coursedetail.if_collect_course(driver, cfg)
            if not ifcollected:
                print u"---取消收藏成功"
                coursedetail.click_back_btn(driver, cfg)
    
    time.sleep(2)
    currentcollecttitlelist = mycollect.get_list_titles()
    theCurrentFirstCourseTile = currentcollecttitlelist[0]
    
    if title != theCurrentFirstCourseTile:
        return True
    else:
        return False
    '''
       
'''   
#收藏课程后点击我的收藏内该课程
def open_course_detail_from_my_collect_page_after_collected_this_course(driver, cfg):
    #��¼
    login.login_by_username(self.cfg, self.driver, self.username_num, self.username_pwd)
    time.sleep(3)
    #���ҵ�ҳ��
    index = Index(self.driver, self.cfg)
    index.click_tab_myself_btn()
    #���ҵĿγ�ҳ��
    mycenter.open_my_course_page(self.driver, self.cfg)
    #�����һ���㲥�γ�
    mycourse.click_my_course_page_dianbo_list_item(self.driver, self.cfg)
    #�жϿγ��Ƿ��ղ�
    ifcollect = coursedetail.if_collect_course(self.driver, self.cfg)
    if 1 == ifcollect:
        coursedetail.click_collect_icon(self.driver, self.cfg)
    #��ȡ�γ�title
    coursetitle = coursedetail.get_course_title(self.driver, self.cfg)
    #�ر�����ҳ�淵���ҵĿγ�ҳ��
    coursedetail.click_back_btn(self.driver, self.cfg)
    #�ر��ҵĿγ�ҳ�淵���ҵ�ҳ��
    mycourse.click_back_btn(self.driver, self.cfg)
    #����ҵ��ղ�
    mycenter.open_my_collect(self.driver, self.cfg)
    #���ҵ��ղ��б����ո��ղصĿγ̽�������ҳ
    ifopencoursedetail = mycollect.open_course_detail_which_course_click_collect_icon(self.driver, self.cfg, coursetitle)
    #�ر�����ҳ�淵���ҵĿγ�ҳ��
    if 1 == ifopencoursedetail:
        coursedetail.click_back_btn(self.driver, self.cfg)
    #�ر��ҵĿγ�ҳ�淵���ҵ�ҳ��
    mycollect.click_back_btn(self.driver, self.cfg)
    #�ص���ҳ
    index.click_tab_home_btn()
    #����л���У��ť
    index.click_change_school_btn()
    #����л��ʺŰ�ť�˳���¼
    myschool = Myschool(self.driver, self.cfg)        
    myschool.click_switchaccount_btn()
    
'''