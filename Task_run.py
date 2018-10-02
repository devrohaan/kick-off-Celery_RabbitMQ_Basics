#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:09:14 2018

@author: rohanbagwe
"""
from Tasks import taskPrintOSName, taskPrintSystem, taskPrintSystemRelease
from time import sleep

if __name__ == "__main__":
    print("** Running Application **")
    result = taskPrintOSName.delay()
    result1 = taskPrintSystem.delay()
    result2 = taskPrintSystemRelease.delay()
    # at this time, our task is not finished, so it will return False
    print("** Applicatoin Completed All tasks are assigned to Celery **")
    print("** Task Completion Check **")
    print('Task finished? ', result.ready(), result1.ready(), result2.ready())
    # False False False
    # sleep 60 seconds to ensure the task has been finished
    sleep(60)
    # now the task should be finished and ready method will return True
    print("** Task Completion Check after 60 seconds **")
    print ('Tasks finished? ', result.ready(), result1.ready(), result2.ready())
    # True True True