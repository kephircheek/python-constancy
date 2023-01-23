# python-constancy
Container for constants.

![test](https://github.com/kephircheek/python-constancy/actions/workflows/main.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/constancy.svg)](https://badge.fury.io/py/constancy)
[![license: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Installing**
```bash
pip install constancy
```

**Example:**
```python
from constancy import Constants
```

Create container for constants

```python
>>> DAYS = Constants(
...     MON=0,
...     TUE=1,
...     WED=2,
...     THU=3,
...     FRI=4,
...     SAT=5,
...     SUN=6
... )
```

Get value from container
```python
>>> DAYS.MON
0
>>> DAYS['MON']
0
```

Represent with pure python data structures
```python
>>> list(DAYS)
['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
>>> dict(DAYS)
{'WED': 2, 'SUN': 6, 'FRI': 4, 'THU': 3, 'MON': 0, 'TUE': 1, 'SAT': 5}
```

All constants are immutable
```python
>>> DAYS.MON = 7
...
AttributeError: Immutable attribute

>>> del DAYS.MON
...
AttributeError: Immutable attribute
```

Autocomplete only for constants
```python
>>> dir(DAYS)
['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
```

Sorting like `list.sort`
```python
>>> DAYS.sort(key=lambda k, v: v, reverse=True)
>>> list(DAYS)
['SUN', 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON']
```
