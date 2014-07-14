#!/usr/bin/env python
#encoding=utf-8

import tornado.ioloop
import tornado.web

#导入包
from app import WebServer

#配置
settings = {'debug' : True}

#路由
application = tornado.web.Application([
    (r"/", WebServer.Home),
    (r"/_req", WebServer.Request),
], **settings)


#初始化
if __name__ == "__main__":
    application.listen(8981)
    tornado.ioloop.IOLoop.instance().start()