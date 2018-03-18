import re

from bsearch.plugins.base import Plugin
from bsearch.utils import base64decode


class UniqueCSP(Plugin):

    CSP = 'Content-Security-Policy'
    CSP_RE = re.compile('Content-Security-Policy: (.*?)\n')

    def __init__(self):
        self.unique_csps = set()

    def process_item(self, item):
        response = base64decode(item.response.get('#text'))
        response = response[:10000]

        if self.CSP not in response:
            return

        mo = self.CSP_RE.search(response)
        if not mo:
            return

        csp = mo.group(0)
        if not csp:
            return

        csp = csp.strip()
        self.unique_csps.add(csp)

    def end(self):
        print('Got %s unique CSP:' % len(self.unique_csps))

        for csp in self.unique_csps:
            print(csp)
