a = 0
a += 1
a += 1
print(a)

def func():
    global a
    a += 1
    a += 1
    a += 1
    print(a)

func()
print(a)