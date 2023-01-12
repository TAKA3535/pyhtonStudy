# リストの組込み関数
# max(リスト名)     ・・・最大値を求める
# min(リスト名)     ・・・最小値を求める
# sum(リスト名)     ・・・合計値を求める
# sorted(リスト名)  ・・・並べ替えをする

# 5-12
store = [2,4,1,9,6]
print("現代のデータ:",store)

print("データの長さ",len(store))
print("最大値データ",max(store))
print("最小値データ",min(store))
print("合計値データ",sum(store))
print("ソートデータ昇順",sorted(store)) 
print("ソートデータ降順",sorted(store,reverse=True)) 