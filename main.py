#!/usr/bin/env python

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def __init__(self):
        super(MainHandler, self).__init__()

    def get(self):
        self.write("Boobs")

app = tornado.web.Application([
    (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()