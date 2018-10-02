#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:09:14 2018

@author: rohanbagwe
"""
from celery import Celery

    
# Create the app and set the broker location (RabbitMQ)
app = Celery('CeleryApp',
             backend='rpc://',
             broker='amqp://rdbagwe:rdbagwe123@localhost/rdbawge_vhost',
             include='Tasks')
