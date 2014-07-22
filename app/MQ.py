#! /usr/bin/env python
# encoding:utf-8

import threading,time,Queue,urllib,hashlib,func

class MQ:
    mq = Queue.Queue()
    callbacks = {}
    
    def __init__(self):
        Worker(self).start();
        Worker(self).start();
    
    def add(self, x):
        data,cal = x;
        tm = "%.2f" % time.time();
        ret = self.callbacks.setdefault(func.parse_request(cal), tm);
        print self.callbacks;
        #使用上次保存的id
        self.mq.put((data,ret), True, None);

    def get(self):
        return self.mq.get();

    def size(self):
        return self.mq.qsize();
    
    def task_done(self):
        return self.mq.task_done();


class Worker(threading.Thread):
    def __init__(self, mq):
        threading.Thread.__init__(self);
        self.daemon = True;
        self.mq = mq;

    def run(self):
        while(True):
            data,call_id = self.mq.get();
            print self.getName() + " receive: " + str(self.mq.size());
            data = func.json_decode(data);
            ret = self.check(data['url']);
            data['_code_'] = ret;
            self.recall(self.get_callback(call_id), data);
            self.mq.task_done();
            
    def get_callback(self,call_id):
        for (k,v) in self.mq.callbacks.iteritems():
            print "find: %s, key: %s, value: %s" % (call_id, k, v);
            if(call_id == v):
                return k;
        return -1;

    def check(self,url):
        file = urllib.urlopen(url).getcode();
        return file;

    def recall(self,url,data):
        if(url != -1):
            func.log("[INFO ][RETURN] url:%s, data: %s" %(url, data));
            urllib.urlopen(url + "?%s" % urllib.urlencode(data)).getcode();
        else:
            func.log("[ERROR][CALLBACK] empty callback, data: %s" % data);