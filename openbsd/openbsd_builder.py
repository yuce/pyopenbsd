
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef('''
    int pledge(const char *promises, const char *execpromises);
    int unveil(const char *path, const char *permissions);
''')

ffibuilder.set_source("openbsd._openbsd",
"""
    #include <unistd.h>
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)


