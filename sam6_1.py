# 6-1 関数の呼び出しP97
def greeting():
    print("おはようございます。")

print("挨拶をしましょう。")
greeting()

# 6-2 関数を何度も呼び出し
def greeting():
    print("おはようございます。")

print("挨拶をしましょう。")
greeting()
print("もう一度")
greeting()

# 6-3　引数を与えてあいさつ関数を呼び出す
def greeting2(who):
    print(who,"さん、おはようございます!!!")

print("挨拶してね")
greeting2("森")

# 6-4　複数の引数の設定
def greeting3(who1,who2):
    print(who1,"さん",who2,"さんおはよう！")

print("挨拶よろ～")
greeting3("もり","モリタ")

# 6-5　引数のない関数
def greeting4():
    print("おっはー")

print("あいさつ～～")
greeting4()