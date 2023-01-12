# P80 リストを逆順に表示
# 1.    リスト名[::-1]
# 2.    reversed(リスト名)
# 3.    リスト名.revers()


store = [1,2,3,4,5,]
print("変更前:",store)

scrap1 = store[::-1]
print("store:",store)
print("scrap1]",scrap1)

# reverseの戻り値はnoneなことに注意すること
scrap2 = store.reverse()
print("store:",store)
print("store2:",scrap2)