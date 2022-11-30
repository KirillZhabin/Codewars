# https://www.codewars.com/kata/5da558c930187300114d874e

from collections import namedtuple
import unicodedata

def create_namedtuple_cls(cls_name, fields):
    cls = namedtuple(cls_name, fields)
    fs = {unicodedata.normalize('NFKC', k): k for k in fields}
    def get(self, k):
        if k in fs:
            return getattr(self, fs[k])
        raise AttributeError
    cls.__getattr__ = get
    return cls