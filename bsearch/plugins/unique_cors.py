import re

# try to import C parser then fallback in pure python parser.
try:
    from http_parser.parser import HttpParser
except ImportError:
    from http_parser.pyparser import HttpParser

from bsearch.plugins.base import Plugin
from bsearch.utils import base64decode


class UniqueCORS(Plugin):

    CORS_RE = re.compile('Access-Control-(.*?)')

    def __init__(self):
        self.unique_cors = set()

    def process_item(self, item):
        response_text = item.response.get('#text')
        if response_text is None:
            return

        response = base64decode(response_text)
        response = response.encode('ascii', errors='ignore')

        p = HttpParser()
        p.execute(response, len(response))

        matching_headers = []

        for header, value in p.get_headers().iteritems():
            if self.CORS_RE.search(header):
                matching_headers.append((header, value))

        if not matching_headers:
            return

        headers_str = '\n'.join(sorted('%s: %s' % (k, v) for (k, v) in matching_headers))
        self.unique_cors.add(headers_str)

    def end(self):
        print('Got %s unique CORS:\n' % len(self.unique_cors))

        for matching_headers in self.unique_cors:
            print(matching_headers)
            print('\n\n')
