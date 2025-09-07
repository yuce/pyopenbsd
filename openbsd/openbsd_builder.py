
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef('''
    int pledge(const char *promises, const char *execpromises);
    int unveil(const char *path, const char *permissions);
    int sysctl(const int *name, unsigned namelen, void *oldp, size_t *oldlenp,
         void *newp, size_t newlen);
    void perror(const char *string);
''')

ffibuilder.set_source("openbsd._openbsd",
"""
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <sys/sysctl.h>
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)


