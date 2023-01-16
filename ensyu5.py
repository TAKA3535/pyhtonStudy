###演習５

#参照リスト
taro = [88,91,92,100]
jiro = [47,51,62,31]
saburo = [98,38,87,85]
hanako = [97,99,85,100]
haruko = [96,85,40,85]
natuko = [87,73,73,70]



##5-1
print("太郎の最高点は",max(taro),"です。最低点は",min(taro),"です。合計点は",sum(taro),"です。")
print("次郎の最高点は",max(jiro),"です。最低点は",min(jiro),"です。合計点は",sum(jiro),"です。")
print("三郎の最高点は",max(saburo),"です。最低点は",min(saburo),"です。合計点は",sum(saburo),"です。")
print("花子の最高点は",max(hanako),"です。最低点は",min(hanako),"です。合計点は",sum(hanako),"です。")
print("春子の最高点は",max(haruko),"です。最低点は",min(haruko),"です。合計点は",sum(haruko),"です。")
print("夏子の最高点は",max(natuko),"です。最低点は",min(natuko),"です。合計点は",sum(natuko),"です。")



##5-2
jpn = [taro[0],jiro[0],saburo[0],hanako[0],haruko[0],natuko[0]]
math = [taro[1],jiro[1],saburo[1],hanako[1],haruko[1],natuko[1]]
science = [taro[2],jiro[2],saburo[2],hanako[2],haruko[2],natuko[2]]
history = [taro[3],jiro[3],saburo[3],hanako[3],haruko[3],natuko[3]]

print("国語の最高点は",max(jpn),"です。最低点は",min(jpn),"です。平均点は",sum(jpn)/6,"です。")
print("算数の最高点は",max(math),"です。最低点は",min(math),"です。平均点は",sum(math)/6,"です。")
print("理科の最高点は",max(science),"です。最低点は",min(science),"です。平均点は",sum(science)/6,"です。")
print("社会の最高点は",max(history),"です。最低点は",min(history),"です。平均点は",sum(history)/6,"です。")



##5-3
taro.append(int(input("太郎の英語の点数を入力してください。")))
jiro.append(int(input("次郎の英語の点数を入力してください。")))
saburo.append(int(input("三郎の英語の点数を入力してください。")))
hanako.append(int(input("花子の英語の点数を入力してください。")))
haruko.append(int(input("春子の英語の点数を入力してください。")))
natuko.append(int(input("夏子の英語の点数を入力してください。")))
eng = [taro[4],jiro[4],saburo[4],hanako[4],haruko[4],natuko[4]]
print("英語の最高点は",max(eng),"です。最低点は",min(eng),"です。平均点は",sum(eng)/6,"です。")



##5-4
#参照リスト
score = [
    [88,91,92,100],
    [47,51,62,31],
    [98,38,87,85],
    [97,99,85,100],
    [96,85,40,85],
    [87,73,73,70],
    ]
student = ["太郎","次郎","三郎","花子","春子","夏子"]
subject = ["国語","算数","理科","社会"]


##5-4-1
for i in range(len(score)):
    print(student[i],"の最高点は",max(score[i]),"です。最低点は",min(score[i]),"です。合計点は",sum(score[i]),"です。")

print()



###5-4-2
#科目ごとのリストを入れる空リスト
score2 = []
#科目ごとの表を作るための行列変換
for i in range(len(score[0])):
    tmp = []
    for j in score:
        tmp.append(j[i])
    score2.append(tmp)

for i in range(len(score2)):
    print(subject[i]," の最高点は ",max(score2[i]),"です。最低点は",min(score2[i]),"です。平均点は",sum(score2[i])/6,"です。")

print()



##5-4-3
subject.append("英語")
#英語の点数入力
for i in range(len(score)):
    print(student[i],end="")
    score[i].append(int(input("の英語の点数を入力してください。")))
#科目ごとの表作成
score2 = []
for i in range(len(score[0])):
    tmp = []
    for j in score:
        tmp.append(j[i])
    score2.append(tmp)
print(subject[4],"の最高点は",max(score2[4]),"です。最低点は",min(score2[4]),"です。平均点は",sum(score2[4])/6,"です。")
print()



##5-5
data = {}  #答え：C
data = { "orange" : 30 } #答え：C
data = ( "tokyo" , "oosaka" , "nagoya" ) #答え：B 
data = [ 7, 5, 2, 3, 2] #答え：A
data = ({'mark':'スペード','number':'5'}) #答え：BC
data = {(11,12),(21,22),(31,32)} #答え：BC
data =(["消防",119],["警察",110]) #答え：AB



##5-6
data = {"key1":30,"key2":40}
print(data["key3"])
#答え：key3 は存在しない

data = ( "tokyo" , "oosaka" , "nagoya" )
data.append("fukuoka")
#答え：タプルに要素の追加はできない

data = [74,85,69,77,81]
print(data[5])
#答え：Index エラー

data = { "tokyo" , "oosaka" , "nagoya" }
print(data["tokyo"])
#答え：tokyo に値がない