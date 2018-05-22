"""
pathtree
"""

from __future__ import print_function
import os
import sys

PATH_SEP = os.path.sep


class Chars(object):
    VRT = '│   '
    HRZ = '├── '
    CRN = '└── '
    NLN = '\n'


class Node(object):

    def __init__(self, name):
        self.name = name
        self.subs = {}

    def add(self, name):
        if name not in self.subs:
            self.subs[name] = Node(name)
        return self.subs[name]

    def _dump_lines(self, ctx):
        prefix = ''.join(ctx['prefix'])
        ctx['result'].append(prefix + self.name)
        keys = sorted(self.subs.keys())
        for key in keys:
            sub = self.subs[key]
            ctx['prefix'].append('- ')
            sub._dump_lines(ctx)
            ctx['prefix'].pop()

    def dump_lines(self):
        ctx = {
            'prefix': [],
            'result': [],
        }
        self._dump_lines(ctx)
        return ctx['result']

    def __str__(self):
        result = ''
        first = True
        for sub in self.subs.values():
            result += ('' if first else ', ') + str(sub)
            first = False
        if result:
            result = ': {{ {} }}'.format(result)
        return self.name + result


class Tree(object):

    def __init__(self):
        self.root = None

    def split_path(self, path):
        return filter(lambda s: s, path.split(PATH_SEP))

    def add_path(self, path):
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        node = self.root
        for seg in self.split_path(path):
            if node is None:
                node = self.root = Node(seg)
                continue
            if node.name == seg:
                continue
            else:
                node = node.add(seg)

    def dump(self):
        if self.root is None:
            return ''
        else:
            return '\n'.join(self.root.dump_lines())

    def __str__(self):
        return str(self.root)


if __name__ == '__main__':
    tree = Tree()
    for line in sys.stdin:
        tree.add_path(line.strip())
    print(tree.dump())
