import dis

def myfunc():
    return 6 / 2

# Hacking the code object

co = myfunc.__code__

bcode = co.co_code
bcode = list(bcode)
bcode[6] = "\x17"
bcode = "".join(bcode)

import new

co2 = new.code(co.co_argcount,
               co.co_nlocals,
               co.co_stacksize,
               co.co_flags,
               bcode,
               co.co_consts,
               co.co_names,
               co.co_varnames,
               co.co_filename,
               co.co_name,
               co.co_firstlineno,
               co.co_lnotab)

# Injecting the modified code object

myfunc.__code__ = co2

print myfunc()
