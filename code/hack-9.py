myvarnames = ("a", "b")
mycode = ("\x7C"   # LOAD_FAST
          "\x00"   # 0x0000
          "\x00"   # 
          "\x7C"   # LOAD_FAST
          "\x01"   # 0x0001
          "\x00"   #
          "\x17"   # BINARY_ADD
          "\x53")   # RETURN_VALUE

import new

co = new.code(2,         # co_argcount,
              2,         # co_nlocals,
              2,         # co_stacksize,
              0,         # co_flags,
              mycode,    # co_code,
              (),        # co_consts,
              (),        # co_names
              myvarnames,# co_varnames
              "test.py", # co_filename,
              "myfunc",  # co_name,
              0,         # co_firstlineno,
              "")        # co_lnotab


myfunc = new.function(co, {})

print myfunc("abc", "def")
