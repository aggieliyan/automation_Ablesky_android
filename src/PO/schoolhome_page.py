# -*- coding: UTF-8 -*-
'''
Created on 2018-8-10

@author: ablesky
'''
from PO.base import Base

class SchoolHome(Base):
  
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.dr = driver
        #ctxlist = self.dr.contexts
        #print "org ctx:",ctxlist
        
    def get_org_title(self):
        ele = self.dr.find_element(self.cfg.get('org_home_page', 'org_home_page_org_name_by'), \
                             self.cfg.get('org_home_page', 'org_home_page_org_name'))
        return ele.text
