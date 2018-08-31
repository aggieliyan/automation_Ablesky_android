# -*- coding: UTF-8 -*-
'''
Created on 2018-8-21

@author: ablesky
'''
from PO.download_page import DownloadPage
import time

def click_back_btn(driver,cfg):
    download = DownloadPage(driver,cfg)
    download.click_back_btn()

    
'''
清空下载列表
'''    
def clear_download_list(driver,cfg):
    download = DownloadPage(driver,cfg)
    try:
        downloadlist = download.get_download_list()
        if downloadlist:
            download.click_edit_btn()
            download.click_selete_all_btn()
            download.click_delete_btn()
            download.click_delete_sure_btn()
    except:
        time.sleep(2)
        pass
    finally:
        download.click_back_btn()
        
    
'''
验证课件是否添加下载成功
'''
def course_add_download_page_success(driver,cfg,courseTitle):
    download = DownloadPage(driver,cfg)
    list = download.get_all_download_course_title_list()
    list_len = len(list)
    
    flag = False
    i = 0
    while i < list_len:
        if(courseTitle == list[i]):
            flag = True
            break
        i = i + 1
    
    return flag
    '''
    if list_len:
        downloadlist = download.get_download_list()
        downloadlist[item].click()
        return 1
    else:
        return 0
    '''

    
'''
点击播放下载完成的课件
'''
def play_the_download_finish_courseware(driver,cfg):
    download = DownloadPage(driver,cfg)
    #获取课件下载进度列表
    speedlist = download.get_all_download_courseware_current_speed_list()
    #获取课件列表
    coursewarelist = download.get_download_courseware_list()
    list_len = len(speedlist)
    
    flag = False
    i = 0
    while i < list_len:
        if(u"下载完成" == speedlist[i]):
            coursewarelist[i].click()
            time.sleep(15)
            driver.press_keycode(4)
            flag = True
            break
        i = i + 1
    return flag