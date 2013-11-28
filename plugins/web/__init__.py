import plugins.base


class site_web(plugins.base.web):
    STORE_UNREF = True
    PATH = r"/"

    def get(self):
        self.show("main")
