def myfunc():
    return 6 / 2

co = myfunc.__code__
print co.co_consts
print repr(co.co_code)



