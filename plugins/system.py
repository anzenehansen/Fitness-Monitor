import imp
import os

PluginFolder = "./plugins"
MainModule = "__init__"

def get_plugins(folder_exclude=[]):
    plugins = []

    listing = os.listdir(PluginFolder)

    loader = "%s.py" % MainModule

    for item in listing:
        loc = os.path.join(PluginFolder, item)

        if os.path.isdir(loc) and loader in os.listdir(loc):
            info = imp.find_module(MainModule, [loc])
            plugins.append({"name" : item, "info" : info})

    return plugins

def load_plugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])

def web_plugins(exclude=[]):
    wpref = []

    for item in get_plugins(exclude):
        print "Loading plugin: %s" % item["name"]
        wpref.append(load_plugin(item))

    return wpref