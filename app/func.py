#! /usr/bin/env python
# encoding:utf-8
import time,os,json

def log(str):
    ltime = time.localtime(time.time());
    tm = time.strftime('%Y-%m-%d %H:%M:%S',ltime);
    log = "[" + tm + "]" + str;
    filename = "./log/log." + time.strftime('%Y-%m-%d', ltime);
    logfile = open(filename,'w');
    logfile.write(log + "\n");
    logfile.close();
    print log;

def json_encode(obj):
    return json.dumps(obj);


def json_decode(str):
    return json.loads(str);

def parse_request(url):
    ret = url;
    pos = url.find('?');
    if(pos > -1):
        ret = url[0:pos];
    return ret;