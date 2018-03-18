from __future__ import unicode_literals
from __future__ import print_function


import xmltodict

from bsearch.plugin_manager import get_plugin_instance


def main(args):
    plugin = get_plugin_instance(args.plugin)
    search_http_history(args.filename, plugin)
    plugin.end()


def search_http_history(filename, plugin):
    with open(filename, 'rb') as f:
        return xmltodict.parse(f,
                               item_depth=2,
                               item_callback=plugin.process)
