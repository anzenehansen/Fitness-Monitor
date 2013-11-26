from plugins.base import web


class site_web(web):

    def __init__(self, db_ref=None):
        super(site_web, self).__init__(db_ref)
        self.handle = r"/"
        self.title = "Sweet"