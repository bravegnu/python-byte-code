### START: full.py
import dis

### START: disas.py
def disas(code):
    bcode = code.co_code
    state = "opcode"

    for op in bcode:
        op = ord(op)
        if state == "opcode":
            print hex(op), dis.opname[op]
            if op > dis.HAVE_ARGUMENT:
                state = "arg1"
        elif state == "arg1":
            print hex(op)
            state = "arg2"
        elif state == "arg2":
            print hex(op)
            state = "opcode"
### END: disas.py

def myfunc():
    return 6 / 2

disas(myfunc.__code__)
### END: full.py
