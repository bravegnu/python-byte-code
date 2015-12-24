def myfunc():
    return 6 / 2

co = myfunc.__code__

import binascii
import dis

print co.co_consts
print binascii.hexlify(co.co_code)

