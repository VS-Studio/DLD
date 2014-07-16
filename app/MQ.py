#! /usr/bin/env python
# encoding:utf-8

import threading,time,Queue,urllib

class MQ:
    mq = Queue.Queue()
    
    def __init__(self):
        Worker(self).start();
    
    def add(self, x):
        self.mq.put(x, True, None);

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
            url,callback_url = self.mq.get();
            print "receive: " + str(self.mq.size());
            ret = self.check(url);
            self.recall(callback_url + "&code=%s" % ret);
            self.mq.task_done();
        
    def check(self,url):
        file = urllib.urlopen(url).getcode();
        return file;

    def recall(self,url):
        print url;
        urllib.urlopen(url).getcode();