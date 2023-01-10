# P57 4-5 while文
i = 1
while i <= 10:
    print(i,"回目のループです。")
    i += 1

# for文のネスト
for i in range(3):
    for j in range(3):
        print("i:",i,"j:",j)

for i in range(1,4):
    for j in range(1,4):
        print(i*j)

# 4-7
c = False
for i in range(3):
    for j in range(5):
        if c == False:
            print("+", end="")
            c = True
        else:
            print("*", end="")
            c = False
    print()