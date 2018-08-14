'''
Created on 2018-8-14

@author: ablesky
'''
import os
path = os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
for prefix, dirs, files in os.walk(path):
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            os.remove(filename)