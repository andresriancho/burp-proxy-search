import base64
import sys


def base64decode(line):
    decoded = base64.b64decode(line)
    replace = 'backslashreplace' if sys.version_info[0] >= 3 else 'replace'
    return decoded.decode('UTF-8', errors=replace)
