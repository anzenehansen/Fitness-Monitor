#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
import sqlite3 as sqlite
import plugins.system as systemp


settings = dict()

handlers = [
    (r"/css/(.*)", tornado.web.StaticFileHandler,
        {"path": "./templates/bootstrap/css"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler,
        {"path": "./templates/bootstrap/js"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler,
        {"path": "./templates/bootstrap/img"})
    ]

plugins = systemp.load_plugins()
print "Plugins loaded:",plugins
db = sqlite.connect('collection.db')

cur = db.cursor()

opts = {}

print "looping plugins"
for cls,dat in systemp.web_plugins().iteritems():
    ref = dat['ref']

    if hasattr(ref, 'get_opts'):
        opts = ref.OPTS
    opts.update({"cur": cur, "db": db})

    if hasattr(ref, 'PATH'):
        handlers.append((
            ref.PATH, ref, opts
            ))
print "done."


class MainHandler(tornado.web.RequestHandler):

    def __init__(self):
        super(MainHandler, self).__init__()

    def get(self):
        self.write("Boobs")

print "Handlers:",handlers
app = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    db.close()
