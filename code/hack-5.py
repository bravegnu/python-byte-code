### START: full.py
### START: myfunc.py
def myfunc():
    return 6 / 2
### END: myfunc.py

# Modifying the code object
### START: hack.py
import new

co = myfunc.__code__
myconsts = (None, 10, 2)
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
### END: hack.py

# Injecting the code object
### START: inject.py
myfunc.__code__ = co2

print myfunc()
### END: inject.py
### END: full.py
