# 5-9 2種類のリストの連結
store1 = [1,2,3,4]
store2 = [5,6,7,8]
store3 = store1
store1 = store1 + store2
print("store1:",store1)
print("store2:",store2)
print("store3:",store3)

store4 = [1,2,3,4]
store5 = [5,6,7,8]
store6 = store4
store4.extend(store5)
print("store4:",store4)
print("store5:",store5)
print("store6:",store6)

store7 = [1,2,3,4]
store8 = [5,6,7,8]
store9 = store7
store7 = store8
print("store7:",store7)
print("store8:",store8)
print("store9:",store9)