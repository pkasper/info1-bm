# use global variables as little as possible!!!
GLOBAL1 = "available for everyone"

def read_global_variable():
    print(GLOBAL1)
    print(GLOBAL1 * 2)

def write_global_variable():
    global GLOBAL1
    print(GLOBAL1)
    GLOBAL1 = 43
    GLOBAL1 = GLOBAL1 - 1

read_global_variable()
print(GLOBAL1)
write_global_variable()
print(GLOBAL1)
