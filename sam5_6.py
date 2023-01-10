# 5-6　リスト要素の削除
store = [10,50,65,84,10]
print("変更前",store)

a = int(input("何番目のデータを削除しますか"))
del store[a]
print("変更後1:",store)

print("10を削除します。")
store.remove(10)
print("変更後2:",store)

# 5-7 リストをアドレス渡しするプログラムの作成
store = [10,50,65,84,10]
copyList1 = store
store[0] = 77
print("リストの値渡しを使い0番目を変更します。")
print("storeのデータ:",store)
print("copyList1のデータ:",copyList1)

# 5-8
store = [10,50,65,84,10]
copyList2 = list(store)
store[1] = 88
print("リスト()を使い１番目を変更します。")
print("storeのデータ:",store)
print("copyList2のデータ:",copyList2)

store = [10,50,65,84,10]
copyList3 = store.copy()
store[2] = 99
print(".copyを使い2番目を変更します。")
print("storeのデータ:",store)
print("copyList3のデータ:",copyList3)