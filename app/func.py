#! /usr/bin/env python
# encoding:utf-8
import time,os

def log(str):
    ltime = time.localtime(time.time());
    tm = time.strftime('%Y-%m-%d %H:%M:%S',ltime);
    log = "[" + tm + "]" + str;
    filename = "./log/log." + time.strftime('%Y-%m-%d', ltime);
    logfile = open(filename,'w');
    logfile.write(log + "\n");
    logfile.close();
    print log;
