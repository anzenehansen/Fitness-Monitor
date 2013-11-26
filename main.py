#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import sqlite3 as sqlite
import plugins.system as plugins
import plugins.base.web
import sys


sys.path.extend("plugins/")

plugins.import_plugins("plugins/")

db = sqlite.connect('collection.db')

cur = db.cursor()

print "looping plugins"
for cls in plugins.itersubclasses(plugins.base.web):
    print cls.__name__
print "done looping"

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