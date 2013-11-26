import tornado.web


class web(tornado.web.RequestHandler):

    def __init__(self, dbref=None):
        super(web, self).__init__()

        self.handle = r"/"
        self.title = "Home"
        self.db = dbref