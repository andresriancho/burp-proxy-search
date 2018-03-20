from bsearch.plugins.unique_csp import UniqueCSP
from bsearch.plugins.unique_cors import UniqueCORS

DEFAULT_PLUGIN = 'unique_csp'

PLUGINS = {DEFAULT_PLUGIN: UniqueCSP,
           'unique_cors': UniqueCORS}


def get_default_plugin():
    return DEFAULT_PLUGIN


def get_plugin_names():
    return PLUGINS.keys()


def get_plugin_instance(chosen_plugin_name):
    if chosen_plugin_name not in PLUGINS:
        raise Exception('Unknown plugin %s' % chosen_plugin_name)

    return PLUGINS[chosen_plugin_name]()
