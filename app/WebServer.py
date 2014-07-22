#!/usr/bin/env python
#encoding=utf-8

import Base
import func

class Home(Base.Handler):
    def get(self):
        self.write("Welcome DlD v1.0\n");
        
class Test(Base.Handler):
    def get(self):
        print "callback: " + self.get_argument("_code_",'404');
        



class Request(Base.Handler):
    def get(self):
        data = self.get_argument("data","{}");
        callback = self.get_argument("callback","");

        self.get_mq().add((data,callback));
        info = "[REQUEST] data: " + data + ", callback: " + callback;
        func.log(info);
        self.write(info);
        
        
        
        