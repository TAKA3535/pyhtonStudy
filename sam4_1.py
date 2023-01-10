# P50 if文 4-1
num = int(input("数字を入力してください。"))
if num >= 100:
    print("100以上を入力しました")

print("終了します。")

# 4-2 if~elif~else
money = int(input("所持金を入力してください。"))
if money >= 10000:
    print("10000円以上持っています。")
elif money >= 5000:
    print("5000円以上持っています。")
else:
    print("あまりお金を持っていません。")

print("終了します。")
