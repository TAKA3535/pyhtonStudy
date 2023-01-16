# P113 6-8変数の記憶寿命を知る
a = 0

def func():
    global a
    b = 0

    print("変数a:",a,"変数b:",b)
    a += 1
    b += 2
    print("変数 a+1:",a,"変数 b+1:",b)

for i in range(5):
    func()
#変数bは関数が呼び出されるたびに最初に0が格納され、関数の終了ごとに箱が廃棄される
print(a)