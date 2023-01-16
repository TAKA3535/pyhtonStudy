# 6-5戻り値
def cashiers(name, price, number):
    print(name,"を",price,"円で",number,"個の注文です。")
    sum = price * number
    return sum

total = cashiers("ノート", 100, 5)
print("お会計は", total, "円です。")

# 6-6　複数の戻り値を返すプログラム
def cashiers():
    y = 2019
    m = 1
    d = 1
    return y,m,d

sellY, sellM, sellD = cashiers()    #アンパック代入
print("販売日:", sellY, sellM, sellD)
