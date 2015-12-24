myconsts = (None, "Hello Byte Code World!")
mycode = ("\x64"   # LOAD_CONST
          "\x01"   # 0x0001
          "\x00"   # 
          "\x47"   # PRINT_ITEM
          "\x48"   # PRINT_NEWLINE
          "\x64"   # LOAD_CONST
          "\x00"   # 0x0000
          "\x00"   #
          "\x53")   # RETURN_VALUE

import new

co = new.code(0,         # co_argcount,
              0,         # co_nlocals,
              1,         # co_stacksize,
              0,         # co_flags,
              mycode,    # co_code,
              myconsts,  # co_consts,
              (),        # co_names
              (),        # co_varnames
              "test.py", # co_filename,
              "myfunc",  # co_name,
              0,         # co_firstlineno,
              "")        # co_lnotab)


myfunc = new.function(co, {})

myfunc()
