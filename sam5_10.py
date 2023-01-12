# P79 スライスを使ってリストの中から要素を切り出す
#  リストのスライス:    リスト名[開始直:停止値:間隔]
store = [1,2,3,4,5,6,7,8,9,10]
print("変更前:",store)

scrap1 = store[0:5]
print("scrap1:",scrap1)

scrap2 = store[5:]
print("scrap2:",scrap2)

scrap3 = store[::2]
print("scrap3:",scrap3)

store[:5] = [0,0,0,0,0]
print("store:",store)

store[0:2] = [11,12,13,14,15]
print("store:",store)

store[1:3] = [11,12,13,14,15]
print("store:",store)

