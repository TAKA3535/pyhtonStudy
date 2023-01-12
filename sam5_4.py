# 5-4 リストの要素の値を変更するプログラム
store = [10,50,65,84,10]
print("変更前:",store)

a = int(input("何番目のデータを変更しますか?"))
b = int(input("変更後のデータを入力してください。"))

print(a,"番目のデータ",store[a],"を変更します。")
store[a] = b
print("変更後:",store)

# 5-5
store = [10,50,65,84,10]
print("変更前:",store)

a = int(input("追加したい数値を入力してください。"))
store.append(a)
print("変更後１:",store)

# リストに要素追加
print(("store[2]に25を追加"))
store.insert(2,25)
print("変更後2:",store)

