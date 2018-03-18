from dotdict import dotdict


class Plugin(object):

    def process(self, path, http_history):
        if self._path_contains(path, 'items'):
            self.process_item(dotdict(http_history))
        return True

    def process_item(self, item):
        raise NotImplementedError

    def _path_contains(self, path, attr):
        for (k, v) in path:
            if k == attr:
                return True

        return False
