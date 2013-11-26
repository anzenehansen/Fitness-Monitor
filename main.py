#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import sqlite3 as sqlite
import plugins.system as systemp


plugins = systemp.get_plugins()

db = sqlite.connect('collection.db')

cur = db.cursor()

print "looping plugins"
for cls in systemp.web_plugins():
    print cls.__name__
print "done."


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

    db.close()