# # 演習4-1
for i in range(21,31):
    if ((i % 2) == 0):
        print(i,"は偶数です。")
    else:
        print(i,"は奇数です。")

# # 演習4-2
msg = "****"
for i in range(2):
    for j in range(2):
        print(msg)
# 強引だがしたのでも行けた演習4-2
c = False
for i in range(4):
    for j in range(4):
        if c == False:
            print("*", end="")
            c = True
        else:
            print("*", end="")
            c = False
    print()

# 演習4-3
msg = "*"
for i in range(2):
    for j in range(2):
        print(msg)
        msg += "*"

# 演習4-４
white = "□"
black = "■"
num = int(input("表示したいヨコ縞模様の一辺の大きさを入力してください。"))
for i in range(num):
    for j in range(num):
        if i % 2 == 0:
            print(black, end=" ")
        else:
            print(white, end=" ")
    print()

    # 演習4-5
    # white = "□"
# black = "■"
# num = int(input("表示したいタテ縞模様の一辺の大きさを入力してください。\n"))
# for i in range(num):
#     for j in range(num):
#         if j % 2 == 0:
#             print(black, end=" ")
#         else:
#             print(white, end=" ")
#     print()

    # 演習4-6
    # white = "□"
# black = "■"
# num = int(input("表示したいチェック模様の一辺の大きさを入力してください。\n>>"))
# for i in range(num):
#     for j in range(num):
#         if j % 2 == i % 2:
#             print(black,end=" ")
#         else:
#             print(white, end=" ")
#     print()

    # 演習4-7