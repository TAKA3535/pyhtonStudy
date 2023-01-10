# # P61 4-8 break文とcontinue文
# time = int(input("何時の処理で終了しますか?(1~24)"))
# for i in range(24):
#     print(i+1 , "時です。")
#     if(i+1) == time:
#         break

# 4-9 continueぶんで一部の処理のループを飛ばす
time = int(input("何時の処理を飛ばしますか?(1~24)"))
for i in range(24):
    if(i+1) == time:
        continue
    print(i+1 , "時です。")