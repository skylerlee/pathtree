from __future__ import print_function
import sys
from pathtree import Tree


if __name__ == '__main__':
    tree = Tree()
    for line in sys.stdin:
        tree.add_path(line.strip())
    print(tree.dump())
