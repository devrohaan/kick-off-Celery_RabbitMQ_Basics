#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:22:36 2018

@author: rohanbagwe
"""

from CeleryApp import app
import time
import os
import platform

@app.task
def taskPrintOSName():
    
    starttime = time.time()
    print("Hello, taskPrintOSName is started")
    time.sleep(10) #this function is so IO intensive so it takes 10 seconds to process #PUNINTENDED
    print(os.name)
    print("Hello, taskPrintOSName is completed in ", time.time() - starttime, " seconds")

@app.task
def taskPrintSystem():
    
    starttime = time.time()
    print("Hello, taskPrintSystem is started")
    time.sleep(10) #this function is so IO intensive so it takes 10 seconds to process #PUNINTENDED
    print(platform.system())
    print("Hello, taskPrintSystem is completed in ", time.time() - starttime, " seconds")

@app.task
def taskPrintSystemRelease():
    
    starttime = time.time()
    print("Hello, taskPrintSystemRelease is started")
    time.sleep(10) #this function is so IO intensive so it takes 10 seconds to process #PUNINTENDED
    print(platform.release())
    print("Hello, taskPrintSystemRelease is completed in ", time.time() - starttime, " seconds")

