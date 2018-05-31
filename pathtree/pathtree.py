# -*- coding: utf-8 -*-
"""
pathtree
~~~~~~~~
Copyright (C) 2018, Skyler.
Use of this source code is governed by the MIT license that can be
found in the LICENSE file.
"""

from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
from collections import OrderedDict

PATH_SEP = os.path.sep


class Chars(object):
    SPC = '    '
    VRT = '│   '
    JCT = '├── '
    BTM = '└── '


class Node(object):

    def __init__(self, name):
        self.name = name
        self.subs = OrderedDict()

    def add(self, name):
        if name not in self.subs:
            self.subs[name] = Node(name)
        return self.subs[name]

    def _dump_lines(self, result, prefix, cutoff):
        result.append(''.join(prefix) + self.name)
        values = self.subs.values()
        length = len(values)
        for i, sub in enumerate(values):
            last = i == length - 1
            if prefix:
                prefix.pop()
                if cutoff:
                    prefix.append(Chars.SPC)
                else:
                    prefix.append(Chars.VRT)
            if last:
                prefix.append(Chars.BTM)
            else:
                prefix.append(Chars.JCT)
            sub._dump_lines(result, prefix, last)
            prefix.pop()

    def dump_lines(self):
        result = []
        prefix = []
        self._dump_lines(result, prefix, True)
        return result

    def __str__(self):
        result = ''
        first = True
        for sub in self.subs.values():
            result += ('' if first else ', ') + str(sub)
            first = False
        if result:
            result = ': {{ {} }}'.format(result)
        return self.name + result


class Tree(Node):

    def __init__(self, root='.'):
        self.root = root
        super(Tree, self).__init__('.')

    def split_path(self, path):
        return filter(lambda s: s, path.split(PATH_SEP))

    def add_path(self, path):
        path = os.path.relpath(path, self.root)
        node = self
        for seg in self.split_path(path):
            node = node.add(seg)

    def dump_lines(self):
        result = []
        for sub in self.subs.values():
            result.extend(sub.dump_lines())
        return result

    def dump(self):
        return '\n'.join(self.dump_lines())

    def __str__(self):
        return self.dump()


if __name__ == '__main__':
    tree = Tree()
    for line in sys.stdin:
        tree.add_path(line.strip())
    print(tree.dump())
