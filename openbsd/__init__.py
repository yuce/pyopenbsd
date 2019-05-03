
import sys
import os
from cffi import FFI
from ._openbsd import lib as _lib

__all__ = ["pledge", "unveil"]

_ffi = FFI()


def pledge(promises=None, execpromises=None):
    promises = _ffi.NULL if promises is None else _encode(promises)
    execpromises = _ffi.NULL if execpromises is None else _encode(execpromises)
    ret = _lib.pledge(promises, execpromises)
    if ret < 0:
        errno = _ffi.errno
        raise OSError(errno, os.strerror(errno))


def unveil(path=None, permissions=None):
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


