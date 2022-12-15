# https://www.codewars.com//kata/62975e268073fd002780cb0d

from collections import namedtuple
import re

class Type(namedtuple('Type', 'name')):
    def __repr__(self):
        return self.name
    def as_arg_str(self):
        return str(self)
    def __pow__(self, other):
        return Function(self, other)

class Function(namedtuple('Function', 'arg, res'), Type):
    def __repr__(self):
        return f'{self.arg.as_arg_str()} -> {self.res}'
    def as_arg_str(self):
        return f'({self})'
    def __call__(self, arg):
        if arg != self.arg:
            raise TypeError()
        return self.res

def infer_type(context, expression):
    c = re.sub(r'\b[A-Z]\w*', lambda m: f'_("{m[0]}")', context).replace(':', '=').replace('->', '**')
    e = re.sub(r'\w+', lambda m: f'({m[0]})', expression)
    scope = {}
    exec(c, {'_': Type}, scope)
    return str(eval(e, scope))