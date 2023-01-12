# 多次元リスト P83
# 5-13 多次元リストの作成 
# score1 = ["太郎",89,91]
# score2 = ["次郎",50,35]
# score3 = ["花子",100,98]

# scoreList = [score1,score2,score3]

# scores =[
#     ["太郎",89,91],
#     ["次郎",50,35],
#     ["花子",100,98],
# ]

# 5-14 多次元リストの表示
score1 = ["太郎",89,91]
score2 = ["次郎",50,35]
score3 = ["花子",100,98]

scoreList = [score1,score2,score3]
print("scoreList:",scoreList)

scores =[
    ["太郎",89,91],
    ["次郎",50,35],
    ["花子",100,98]
]
print("scores:",scores)

for a in scores:
    print("個人別のデータは",a,"です。")
    for b in a:
        print(b, end="\t")
    print()
    
print(scores[0][0],"君の国語の点数は",scores[0][1],"算数の点数は",scores[0][2],"です。")
print(scores[1][0],"君の国語の点数は",scores[1][1],"算数の点数は",scores[1][2],"です。")
print(scores[2][0],"君の国語の点数は",scores[2][1],"算数の点数は",scores[2][2],"です。")
