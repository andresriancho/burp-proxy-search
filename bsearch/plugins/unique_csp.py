import re
import os

from bsearch.plugins.base import Plugin
from bsearch.utils import base64decode


class UniqueCSP(Plugin):

    CSP = 'Content-Security-Policy'
    CSP_RE = re.compile('Content-Security-Policy: (.*?)\n')
    NONCE_RE = re.compile("'nonce-(.*?)'")
    TARGET = os.environ.get('TARGET', None)

    def __init__(self):
        self.unique_csps = set()

    def process_item(self, item):
        if self.TARGET is not None:
            request = base64decode(item.request.get('#text'))
            request = request[:10000]

            if self.TARGET not in request:
                return

        response_text = item.response.get('#text')
        if response_text is None:
            return

        response_text = base64decode(response_text)
        response_text = response_text[:10000]

        if self.CSP not in response_text:
            return

        mo = self.CSP_RE.search(response_text)
        if not mo:
            return

        csp = mo.group(1)
        if not csp:
            return

        csp = csp.strip()

        # Remove the nonce random string in order to group the same CSP
        csp = self.NONCE_RE.sub('abcdef0987654321', csp)

        # Save
        self.unique_csps.add(csp)

    def end(self):
        print('Got %s unique CSP:\n' % len(self.unique_csps))

        unique_csps = list(self.unique_csps)
        unique_csps.sort()

        for csp in unique_csps:
            print(csp + '\n')
