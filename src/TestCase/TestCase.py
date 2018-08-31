# -*- coding: UTF-8 -*-
'''
Created on 2018-8-28

@author: ablesky
'''

# -*- coding: UTF-8 -*-
'''
Created on 2018-8-10

@author: ablesky
'''


import mycourse
import login
from PO.index_page import Index
from PO.personal_page import Personal
import coursedetail
from PO.base import Base
import play
import download
import examstart
import mycollect
import home

import time

#未登录情况下点击个人中心的快速入口                                  
def testOperateWithoutLogin(self,driver,cfg):
    #判断是否是未登录状态，若登录则退出登录
    username = login.iflogin(driver, cfg)
    if '登录/注册' != username:
        print u"---退出登录"
        login.logout_by_exit_btn(driver,cfg)
    index = Index(driver,cfg)
    base = Base(driver)
    
    print u"切换到首页"
    index.click_tab_home_btn()
    '''try:
        flag = home.isHomePage(driver,cfg)
        self.assertTrue(flag, u"打开首页失败")
        base.switchToNative()
        
    except Exception,e:
        print e
    '''
    print u"切换到能力圈"
    index.click_tab_circle_btn()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击能力圈进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u"切换到会员频道"
    index.click_tab_vip_btn()
        
    print u"切换到交流"
    index.click_tab_communicate_btn()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击交流进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
    
    print u"切换到我的"    
    index.click_tab_myself_btn()
    personalpage = Personal(driver,cfg)
    print u'未登录情况下点击我的课程'        
    personalpage.click_my_course()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击我的课程进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击我的收藏'        
    personalpage.click_my_collect()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击我的收藏进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
    
    print u'未登录情况下点击关注网校'        
    personalpage.click_pay_attention_school()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击关注网校进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击我的下载'        
    personalpage.click_my_download()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击我的下载进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击优惠券'        
    personalpage.click_my_coupon()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击优惠券进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击会员'        
    personalpage.click_my_vip()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击会员进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击账户余额'        
    personalpage.click_balance()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击账户余额进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击推荐有奖'        
    personalpage.click_award()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击推荐有奖进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e
        
    print u'未登录情况下点击分享收益'        
    personalpage.click_share_earning()
    try:
        title = login.get_login_page_title(driver,cfg)
        self.assertEqual(title, u'登录', u'未登录情况下点击分享收益进入登录页面失败')
        login.click_back_btn(driver,cfg)
    except Exception,e:
        print e

    
'''
测试我的收藏页面相关内容：详情页取消收藏，长按取消收藏，清空收藏列表
'''
def testMyCollectPage(self,driver,cfg):
    index = Index(driver, cfg)
    index.click_tab_myself_btn()
    
    personal = Personal(driver, cfg)
    print u"打开我的收藏"
    personal.click_my_collect()

    #从我的收藏进入课程详情页取消收藏课程 
    ifabolish = mycollect.abolish_the_course_of_collection_in_coursedetail(driver, cfg,0)
    self.assertTrue(ifabolish, u'课程取消收藏失败')
    
    #在我的收藏页面长按课程取消收藏课程
    cancelAbolishSuccess = mycollect.abolish_the_course_of_collection_by_longclick(driver, cfg,0)
    self.assertTrue(1 == cancelAbolishSuccess, u"长按取消收藏课程失败")
    
    #取消收藏列表
    cancelClearFlag = mycollect.click_cancel_btn_after_open_clear_dlg(driver, cfg)
    self.assertTrue(cancelClearFlag, u"取消清空收藏失败")
    
    #清空收藏列表
    noDataFlag = mycollect.click_sure_btn_after_open_clear_dlg(driver, cfg)
    self.assertTrue("暂时没有收藏" == noDataFlag, u'清空收藏列表失败')

    mycollect.click_back_btn(driver, cfg)
        

    
'''
测试我的课程相关内容
'''
def testMyCoursePage(self,driver,cfg):
    index = Index(driver, cfg)
    index.click_tab_myself_btn()
    
    personal = Personal(driver, cfg)
    personal.click_my_course()
    
    #从我的课程点击进入点播课程详情页
    openflag = mycourse.click_my_course_page_dianbo_list_item(driver, cfg)
    self.assertTrue(openflag, u"打开点播课程失败")
    coursedetail.click_back_btn(driver, cfg)
    
    #从我的课程点击进入预售班课程详情页
    openflag = mycourse.click_my_course_page_presell_list_item(driver, cfg)
    self.assertTrue(openflag, u"打开预售班课程失败")
    coursedetail.click_back_btn(driver, cfg)
        
    #从我的课程点击进入网络班课程详情页
    openflag = mycourse.click_my_course_page_network_list_item(driver, cfg)
    self.assertTrue(openflag, u"打开网络班课程失败")
    coursedetail.click_back_btn(driver, cfg)
       
    #从我的课程点击进入面授班课程详情页
    openflag = mycourse.click_my_course_page_face_list_item(driver, cfg)
    self.assertTrue(openflag, u"打开面授班课程失败")
    coursedetail.click_back_btn(driver, cfg)
        
    #从我的课程点击进入直播课程详情页
    openflag = mycourse.click_my_course_page_live_list_item(driver, cfg)
    self.assertTrue(openflag, u"打开直播课程失败")
    coursedetail.click_back_btn(driver, cfg)
        
    #从我的课程点击进入考试卷开始答题页
    openflag = mycourse.click_my_course_page_examination_item(driver, cfg)
    self.assertTrue(openflag, u"打开考试卷失败")
    examstart.click_back_btn(driver, cfg)    
    
    #从我的课程点击进入练习卷开始答题页
    openflag = mycourse.click_my_course_page_exercise_item(driver, cfg)
    self.assertTrue(openflag, u"打开练习卷失败")
    examstart.click_back_btn(driver, cfg)        
        
    #从我的课程点击进入题库开始答题页
    openflag = mycourse.click_my_course_page_question_bank_item(driver, cfg)
    self.assertTrue(openflag, u"打开题库失败")
    examstart.click_back_btn(driver, cfg)
    
    mycourse.click_back_btn(driver, cfg)


'''
测试详情页、播放、下载相关内容
'''
def testCourseDetail(self,driver,cfg):        
    index = Index(driver, cfg)
    #点击我的，切换到我的页面
    index.click_tab_myself_btn()
    print u"测试详情页相关内容、播放、下载等..."
    personal = Personal(driver, cfg)
    #打开下载页面，并清空下载列表      
    personal.click_my_download()
    download.clear_download_list(driver, cfg)
    #打开我的课程页面
    personal.click_my_course()
    #我的课程页面选择点播课，并点击进入到点播课课程详情页       
    mycourse.click_my_course_page_dianbo_list_item(driver, cfg)
    #切换到详情tab
    coursedetail.click_first_tab(driver, cfg)
    base = Base(driver)
    print u"开始测试打开老师详情..."
    #上滑显示老师相关信息
    base.swipeUp(0.75, 0.5, 500)
    try:
        flag = coursedetail.open_teacher_info(driver, cfg, 0)
        time.sleep(2)
        driver.press_keycode(4)
        self.assertTrue(flag, u"打开老师详情页错误")
        #切换回native模式
        base.switchToNative()
        #关闭chromedriver
        base.shutdownChromeDriver()
    except:
        print u"课程详情没有设置老师信息"
    
    
    print u"开始测试打开机构首页"
    coursedetail.click_first_tab(driver, cfg)
    #上滑显示机构相关信息
    base.swipeUp(0.75, 0.5, 500)
    flag = coursedetail.open_org_info(driver, cfg)       
    time.sleep(2)
    driver.press_keycode(4)
    self.assertTrue(flag, u"打开机构首页错误")
    #切换回native模式
    base.switchToNative()
    #关闭chromedriver
    base.shutdownChromeDriver()
    
    print u"开始测试课程标签"
    coursedetail.click_first_tab(driver, cfg)
    try:
        #上滑显示课程标签相关信息
        base.swipeUp(0.75, 0.5, 500)
        flag = coursedetail.open_course_tag(driver, cfg)
        self.assertTrue(flag, u"点击课程标签错误")
    except:
        print u"课程详情没有设置标签"
    
    
    print u"开始测试点击底部推荐课程"
    coursedetail.click_first_tab(driver, cfg)
    #上滑显示推荐课程相关信息
    base.swipeUp(0.75, 0.5, 500)
    try:
        flag = coursedetail.click_bottom_recommend_course(driver, cfg, 0)
        self.assertTrue(flag, u"点击底部推荐课程错误")
    except:
        print u"课程详情没有推荐课程"
    coursedetail.click_back_btn(driver, cfg)
    
    print u"开始测试播放单视频..."
    #搜索课程并打开进入该课程详情页
    mycourse.search_course_and_open_the_course_detail(driver, cfg)
    #切换到目录tab
    coursedetail.click_second_tab(driver, cfg)
    #大屏播放课件
    coursedetail.play_courseware(driver, cfg, 0)
    #关闭大屏播放器
    play.play_video_and_exist(driver, cfg)
    
    print u"开始测试下载课件..."
    #下载全部课件
    coursedetail.download_all_courseware(driver, cfg)
    courseTitle = coursedetail.get_course_title(driver, cfg, "dianbo")
    print u'---关闭课程详情页，打开下载页面'
    driver.press_keycode(4)
    mycourse.click_back_btn(driver, cfg)
    #打开下载页面
    personal.click_my_download()
    flag = download.course_add_download_page_success(driver, cfg, courseTitle)
    self.assertTrue(flag, u'课程添加下载失败')
    while True:
        #有下载完成的课件播放并退出
        flag = download.play_the_download_finish_courseware(driver, cfg)
        if flag:
            break
    download.click_back_btn(driver, cfg)

        
 

