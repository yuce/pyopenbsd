# openbsd

Python bindings for some OpenBSD-specific APIs. Currently the following are supported:

* `pledge`
* `unveil`

## Change Log

### v0.1.0 (2019-05-03)

    * Initial release.

## Installation

Openbsd is on PyPI. You can install it using pip:

    pip install openbsd

### Prerequisites

* OpenBSD 6.4 or better
* Python 3.6 or better OR Python 2.7

## Usage

Import `openbsd` first:
```python
import openbsd
```

### pledge

```python
openbsd.pledge("stdio rpath")
print(open("/etc/resolv.conf"))
```

Try removing the`rpath permission.

### unveil

```python
openbsd.unveil("/etc", "r")
print(open("/etc/resolv.conf"))
```

Try opening `/bin/ksh`.

Use `openbsd.unveil()` to lock down restrictions.


## Similar Projects

* [PyPledge](https://gitlab.com/i80and/pypledge): Python binding for the OpenBSD pledge(2) system call. Uses ctypes.

## License

(c) 2019 Yuce Tekol

[BSD](LICENSE)
