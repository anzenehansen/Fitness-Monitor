import tornado.web
import plugins.system
from sys import argv
from os.path import dirname, realpath


class web(tornado.web.RequestHandler, plugins.system.PluginBase):

    OPTS = {}
    PATH = r""

    def initialize(self, **kwargs):
        self.db = kwargs.get("db", None)
        self.cursor = kwargs.get("cur", None)

    def get_opts(self):
        return OPTS

    def get_template_path(self):
        return "%s/templates" % (dirname(realpath(argv[0])))

    def show(self, templ, **kwargs):
        self.render("%s.html" % templ, **kwargs)
