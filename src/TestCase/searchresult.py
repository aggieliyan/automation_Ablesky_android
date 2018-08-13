# -*- coding: UTF-8 -*-
'''
Created on 2018-8-13

@author: ablesky
'''

from PO.searchresult_page import SearchResult

def click_cancel_btn(driver,cfg):
    searchResult = SearchResult(driver,cfg)
    searchResult.click_cancel_btn()
    
def get_result_list(driver,cfg):
    searchResult = SearchResult(driver,cfg)
    resultList = searchResult.get_result_list()
    return resultList

def get_search_key(driver,cfg):
    searchResult = SearchResult(driver,cfg)
    key = searchResult.get_search_key_text()
    return key