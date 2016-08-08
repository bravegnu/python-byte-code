def myfunc():
    return 6 / 2

co = myfunc.__code__

print "co_consts:",
print co.co_consts

print "co_code:",
print repr(co.co_code)
