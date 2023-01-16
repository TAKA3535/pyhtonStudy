# P109 6-7 変数とスコープ 
a = 0 #グローバル変数a

def funcB():
    b = 1 #ローカル変数b
    print("funcBの中では変数aと変数bが使える")
    print("変数aの値は", a, "です")
    # print("変数cは", c, "です")

def funcC():
    c = 2 #ローカル変数cです
    print("funcCのなかでは変数aと変数cがつかえる")
    print("変数aの値は", a, "です")
    # print("変数bの値は", b, "です")
    print("変数cの値は", c, "です")

print("関数の外で変数aがつかえる")
print("変数aの値は", a, "です")
# print("変数bの値は", b, "です")
# print("変数cの値は", c, "です")

funcB()
funcC()