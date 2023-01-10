# 演習3-1
print("あなたは何歳ですか？")
print("あなたは20歳です。")

# 演習3-2
height = float(input("身長を入力してください。"))/100
weight = float(input("体重を入力してください。"))
print("身長は",height,"cmです。")
print("体重は",weight,"kgです。")
bmi = round((weight / (height ** 2)),2)
print("BMIは",bmi,"です。")

# 演習3-3
name = input("名前を入力してください。")
year = int(input("生まれた年を入力してください。"))
age = 2020 - year
print(name,"さんの年齢は",age,"歳です。")