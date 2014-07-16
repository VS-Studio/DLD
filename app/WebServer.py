#!/usr/bin/env python
#encoding=utf-8

import Base
import func

class Home(Base.Handler):
    def get(self):
        self.write("Welcome DlD v1.0\n");
        
class Test(Base.Handler):
    
    #@tornado.web.asynchronous
    def get(self):
        #self.file_get_content("http://www.baidu.com");
        #self.file_get_content_asyn("http://www.baidu.com", self.callback);
        print "callback: " + self.get_argument("code",'404');
        
    def callback(self,response):
        print "ok"
        print len(response.body)
        self.write("ok")
        self.finish();

class Request(Base.Handler):
    def get(self):
        url = self.get_argument("url","");
        callback = self.get_argument("callback","");
        #print self.json_decode(data);
        self.get_mq().add((url,callback));
        #print self.get_mq().size();
        info = "url: " + url + ", callback: " + callback;
        func.log(info);
        #self.echo_json(self.json_decode(data));
        self.write(info);
        
        
        
        