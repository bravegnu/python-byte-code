def myfunc():
    return 6 / 2

co = myfunc.__code__

import binascii
import dis

print co.co_consts
print binascii.hexlify(co.co_code)

print

i = 0
code = co.co_code
state = "opcode"

for op in code:
    op = ord(op)

    if state == "opcode":
        print "%02X" % op, dis.opname[op]
        if op > dis.HAVE_ARGUMENT:
            state = "arg1"

    elif state == "arg1":
        print "%02X" % op
        state = "arg2"

    elif state == "arg2":
        print "%02X" % op
        state = "opcode"
