# -*- coding: UTF-8 -*-

import time
from selenium.common.exceptions import NoSuchElementException

from appium.webdriver.mobilecommand import MobileCommand
  
class Base():
       
    def __init__(self, driver):
        self.dr = driver
     
    def datatime_now(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        return now
    
    def datatime_day(self):
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return day
    
    def find_element(self, how, what):
        flag = None
        try:
            self.dr.find_element(by=how, value=what)
            flag = True
        except NoSuchElementException,e: 
            flag = False
        finally:
            return flag
    def find_elements(self, how, what):
        flag = None
        try:
            self.dr.find_elements(by=how, value=what)
            flag = True
        except NoSuchElementException,e: 
            flag = False
        finally:
            return flag
    
    def save_screenshot(self):
        filename = self.datatime_now() + '.png'
        self.dr.save_screenshot("C://test_rs_pic//" + filename)
        return filename    
    
    def getSize(self):
        x = self.dr.get_window_size()['width']
        y = self.dr.get_window_size()['height']    
        return (x, y)     
    
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.dr.swipe(x1, y1, x1, y2, t)
        
    def swipDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[2] * 0.75)
        self.dr.swipe(x1, y1, x1, y2, t)
        
    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.dr.swipe(x1, y1, x2, y1, t)
       
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.dr.swipe(x1, y1, x2, y1, t)
    '''
    modified by sdu
    '''
    def switch_h5(self):
        self.dr.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "webview的context名称"})

    def switch_app(self):
        self.dr.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})  
    
    '''
    ended
    '''   
        
# 启动/关闭appium服务
# 
#     def start_Appium(self, host, port, bootstrap_port, appium_log_path): #device_uid,
#         #appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
#         errormsg = ""
#         appium_server_url =""
#         try:
#             if self.port_is_free(host,port):
#                 cmd ='start /b appium -a '+ host +' -p '+ str(port)+ ' --bootstrap-port '+ str(bootstrap_port) +  ' --session-override --log '+ '"'+appium_log_path + '" --command-timeout 600'  #' -U '+ device_uid+
#                 print cmd
#                 #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
#                 p = subprocess.call(cmd, shell=True,stdout=open('E:/logs.log','w'),stderr=subprocess.STDOUT)
#                 print p
#                 appium_server_url = 'http://' + host +':' + str(port) +'/wd/hub'
#                 print appium_server_url
#             else:
#                 print "port:%d is used!"%(port)
#         except Exception, msg:
#             errormsg = str(msg)
#         return appium_server_url, errormsg
#         
#     def stop_Appium(self, Appium_url):
#         cmd = 'StopAppium.bat %s'%(self.get_port(Appium_url))
#         p = os.popen(cmd)
#         print p.read()
       
    

        

    
    
