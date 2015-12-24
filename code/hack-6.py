def myfunc():
    return 6 / 2

co = myfunc.__code__

import binascii
import dis

print co.co_consts
print binascii.hexlify(co.co_code)

print

code = co.co_code
code = list(code)
code[6] = "\x17"
code = "".join(code)

print binascii.hexlify(code)


