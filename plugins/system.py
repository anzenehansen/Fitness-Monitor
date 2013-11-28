import imp
import inspect
import os

PluginFolder = "./plugins"
MainModule = "__init__"

_PLUGINS = {}
_RESERVED = {"files": ["base"]}

class PluginRegistry(type):

    def __init__(self, name, bases, attrs):
        if not name.endswith("Base"):
            try:
                if not self.plugin_disabled:
                    dir_,file_ = os.path.split(os.path.abspath(
                        inspect.getfile(self)[:-1]
                        ))

                    pl_class = self._TYPE

                    if not pl_class in _PLUGINS:
                        _PLUGINS[pl_class] = {}

                    if not name in _PLUGINS[pl_class]:
                        fn, _ = os.path.splitext(file_)

                        ref = self

                        _PLUGINS[pl_class][name] = {'ref': ref, 'loader': fn, 'dir': dir_}

                        if "STORE_ATTRS" in attrs and attrs['STORE_ATTRS'] == True:
                            _PLUGINS[pl_class][name]['attrs'] = attrs
            except AttributeError:
                    pass

class PluginBase(object):
    __metaclass__ = PluginRegistry
    PLUGINS = _PLUGINS
    STORE_ATTRS = False
    plugin_disabled = False
    _TYPE = "web"

    def __init__(self):
        pass

def load_plugins(dir_=PluginFolder, load=True):
    dir_ = os.path.abspath(dir_)

    plugin_info = {}
    path = ""
    plugin = ""
    loc = ""

    for item in os.listdir(dir_):
        loc = os.path.join(dir_, item)

        if os.path.isdir(loc) and "%s.py" % MainModule in os.listdir(loc):
            info = imp.find_module(MainModule, [loc])

            if info[0] and load:
                imp.load_module(MainModule, *info)

    return _PLUGINS

def get_plugins(folder_exclude=[]):
    plugins = []

    listing = os.listdir(PluginFolder)

    loader = "%s.py" % MainModule

    for item in listing:
        loc = os.path.join(PluginFolder, item)

        if os.path.isdir(loc) and loader in os.listdir(loc):
            info = imp.find_module(MainModule, [loc])
            plugins.append({"name": item, "info": info, "loc": loc})

    return plugins

def load_plugin(plugin):
    print "load_plugin(%s)" % (plugin["loc"])
    return imp.load_module(MainModule, *plugin["info"])

def web_plugins(exclude=[]):
    return _PLUGINS["web"]
