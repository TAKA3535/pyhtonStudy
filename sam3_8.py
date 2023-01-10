text = input("好きな文字列を入力してください。")
print(text,"が入力されました。")

# 3-9 これだと入力した文字1列に並ぶだけ
num1 = input("整数1を入力してください。")
num2 = input("整数2を入力してください。")
num3 = num1 + num2
print(num1,"+",num2,"は",num3,"です。")

# 3-10 キャストすることで整数型になる計算可
num1 = int(input("整数1を入力してください。"))
num2 = int(input("整数2を入力してください。"))
num3 = num1 + num2
print(num1,"+",num2,"は",num3,"です。")