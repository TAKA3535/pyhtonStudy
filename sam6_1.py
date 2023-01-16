# 6-1 関数の呼び出しP97
def greeting(): #関数作成
    print("おはようございます。")

print("挨拶をしましょう。")
greeting()  #関数呼び出し

# 6-2 関数を何度も呼び出し
def greeting():
    print("おはようございます。")

print("挨拶をしましょう。")
greeting()
print("もう一度")
greeting()

# 6-3　引数を与えてあいさつ関数を呼び出す
def greeting2(who): #()の中の引数は仮引数
    print(who,"さん、おはようございます!!!")

print("挨拶してね")
greeting2("森") #呼び出しの方の()の中は実引数

# 6-4　複数の引数の設定
def greeting3(who1,who2):
    print(who1,"さん",who2,"さんおはよう！")

print("挨拶よろ～")
greeting3("もり","モリタ")

# 6-1　引数のない関数
def greeting4():
    print("おっはー")

print("あいさつ～～")
greeting4()