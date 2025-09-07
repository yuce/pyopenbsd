
import sys
import os
from typing import Any

from cffi import FFI

from openbsd._openbsd import lib as _lib
from openbsd.const import CTL_HW, HW_NCPU

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


def _sysctl(mib: list[int], ret_type:str, ret_size:int, set_type=None, set_size=0) -> Any:
    if set_type:
        raise ValueError("set_type is not supported")
    else:
        set_type = _ffi.NULL
    fmib = _ffi.new("int[]", mib)
    value = _ffi.new(ret_type)
    size = _ffi.new("size_t*", ret_size)
    ret = _lib.sysctl(fmib, len(mib), value, size, set_type, set_size)
    if ret < 0:
        errno = _ffi.errno
        raise OSError(errno, os.strerror(errno))
    return value[0]
    

def get_cpu_count() -> int:
    """Return CPU count."""
    # TODO: find ptr_size auto
    ptr_size = 8
    return _sysctl([CTL_HW, HW_NCPU], "int*", ptr_size)


def _encode(text):
    if isinstance(text, str):
        return text.encode("ascii")
    return text


