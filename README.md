# pathtree

[![PyPI](https://img.shields.io/pypi/v/pathtree.svg)](https://pypi.org/project/pathtree/)

## Installation

`pip install pathtree`

## Example

* Use in Shell

Run command `find pathtree | python pathtree` will print this:

```txt
pathtree
├── pathtree.py
├── __main__.py
├── __pycache__
│   ├── pathtree.cpython-36.pyc
│   └── __main__.cpython-36.pyc
└── __init__.py
```

* Use Programmatically

```python
from pathtree import Tree

# Init
tree = Tree()
# Add path
tree.add_path(<path>)
# Print tree
print(tree.dump())
```

## License
The MIT License.
