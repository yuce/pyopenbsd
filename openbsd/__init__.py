
import sys
import os
from cffi import FFI
from ._openbsd import lib as _lib

__all__ = ["pledge", "unveil"]
_ffi = FFI()


def pledge(promises=None, execpromises=None):
    """Restrict system operations.
    
    `promises` is a space separated string or binary of promises or `None` for no restrictions.
    `execpromises` has the same format as `promises` and contains promises when runing other binaries using `execve`, etc.

    See: https://man.openbsd.org/pledge.2 for more information.
    """

    promises = _ffi.NULL if promises is None else _encode(promises)
    execpromises = _ffi.NULL if execpromises is None else _encode(execpromises)
    ret = _lib.pledge(promises, execpromises)
    if ret < 0:
        errno = _ffi.errno
        raise OSError(errno, os.strerror(errno))


def unveil(path=None, permissions=None):
    """Unveil parts of a restricted filesystem view.

    `path` may be a string or a binary.
    `permissions` should be a combination of:
    * `r`: Make path available for read operations.
    * `w`: Make path available for write operations.
    * `x`: Make path available for execute operations.
    * `c`: Allow path to be created and removed.

    See: https://man.openbsd.org/unveil.2 for more information.
    """

    path = _ffi.NULL if path is None else _encode(path)
    permissions = _ffi.NULL if permissions is None else _encode(permissions)
    ret = _lib.unveil(path, permissions)
    if ret < 0:
        errno = _ffi.errno
        raise OSError(errno, os.strerror(errno))


if isinstance(b"openbsd", str):
    # Python 2
    def _encode(text):
        if isinstance(text, unicode):
            return text.encode("ascii")
        return text
else:
    # Python 3
    def _encode(text):
        if isinstance(text, str):
            return text.encode("ascii")
        return text


