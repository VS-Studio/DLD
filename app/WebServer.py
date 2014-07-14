#!/usr/bin/env python
#encoding=utf-8

import tornado.ioloop
import tornado.web

class Home(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome \n DlD 333")
        

class Request(tornado.web.RequestHandler):
    def get(self):
        self.write("xxx")
        
        msg = self.get_argument("message","{}")
        
        print tornado.escape.json_decode(msg)
        
        self.write("You wrote " + msg)