#! /usr/bin/env python

from __future__ import print_function
import sys
import os

from openbsd import pledge, unveil

"""
A little utilty that pledges and unveils.
python3 restrict.py rpath stdio /tmp/foo:r /bin/cat:x  -x cat /tmp/foo
"""

def extract_args(args):
    promises = set()
    rviews = []
    cmd_args = []
    eop = False

    for arg in args:
        if eop:
            cmd_args.append(arg)
            continue
        if arg == "-x":
            eop = True
            continue
        if ":" in arg:
            rviews.append(tuple(arg.split(":", 1)[:2]))
        else:
            promises.add(arg)

    promises = None if "ALL" in promises else " ".join(promises)
    return promises, rviews, eop, cmd_args


def print_usage():
        print("Usage: %s [ALL | promise1 promise2 ...] -x cmd [arg1 arg2 ...]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)


def main():
    promises, rviews, eop, cmd_args = extract_args(sys.argv[1:])
    if not eop:
        print_usage()

    if rviews:
        for path, perm in rviews:
            unveil(path, perm)

    pledge("exec stdio rpath", promises)
    os.execvp(cmd_args[0], cmd_args)

if __name__ == "__main__":
    main()

