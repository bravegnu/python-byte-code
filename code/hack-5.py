def myfunc():
    return 6 / 2

co = myfunc.__code__

import binascii
import dis

myconsts = (None, 10, 2)

import new

co2 = new.code(co.co_argcount,
               co.co_nlocals,
               co.co_stacksize,
               co.co_flags,
               co.co_code,
               myconsts,
               co.co_names,
               co.co_varnames,
               co.co_filename,
               co.co_name,
               co.co_firstlineno,
               co.co_lnotab)

myfunc.__code__ = co2

print myfunc()
