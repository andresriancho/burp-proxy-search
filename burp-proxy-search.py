import argparse

from bsearch.plugin_manager import get_plugin_names, get_default_plugin
from bsearch.main import main


DEFAULT_PLUGIN = get_default_plugin()
PLUGINS = get_plugin_names()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Burp suite HTTP history advanced search')

    parser.add_argument('filename', help='Burp Suite HTTP proxy history file')

    parser.add_argument('--plugin',
                        default=DEFAULT_PLUGIN,
                        choices=PLUGINS,
                        help='Analysis plugin to run, default: %s' % DEFAULT_PLUGIN)

    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)
