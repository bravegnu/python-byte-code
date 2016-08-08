def myfunc():
    return 6 / 2

co = myfunc.__code__

print "co_consts:", co.co_consts
print "co_code:"

for i, ch in enumerate(co.co_code):
    print "    %d: %02X" % (i, ord(ch))
