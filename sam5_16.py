# 5-16 ディクショナリ P87
# goods = {"pen":100, "note":130, "eraser":80}
# print("現在のデータ",goods)

# select = input("どの商品の金額を表示しますか?")

# if select in goods:
#     print(select,"の商品の金額は",goods[select],"です。")
# else:
#     print(select,"の商品が見つかりません")

# ■■■
goods = {"pen":100, "note":130, "eraser":80}
print("現在のデータ",goods)

# 商品の追加
key = input("追加する商品キーを入力してください。")

if key in goods:
    print(key,"は既に登録されています。")
else:
    cost = int(input("追加する商品の金額を入力してください。"))
    goods[key] = cost
    print(key,"の金額として",goods[key],"を追加しました。")

print("現在のデータ",goods)

# 商品の変更
key = input("変更する商品キーを入力してください。")

if key in goods:
    print(key,"の金額データは",goods[key],"です。")
    cost = int(input("変更したい金額を入力してください。"))
    goods[key] = cost
    print("現在のデータ",goods)
else:
    print(key,"のデータは見つかりませんでした。")

# 商品の削除
key = input("削除したいデータのキーを入力してください。")

if key in goods:
    print(key,"の金額データは",goods[key],"です。")
    del goods[key]
    print("データを削除しました。")
else:
    print(key,"のデータは見つかりませんでした。")

print("現在のデータ",goods)
