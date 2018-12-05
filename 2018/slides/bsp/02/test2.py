# use global variables as little as possible!!!
GLOBAL1 = 5

def test1():
    test2()
    global GLOBAL1
    GLOBAL1 = GLOBAL1 *2

def test2():
    global GLOBAL1
    GLOBAL1 = GLOBAL1 -1

test1()
print(GLOBAL1)
test2()
print(GLOBAL1)
