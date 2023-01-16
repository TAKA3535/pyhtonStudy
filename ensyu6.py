# P114 演習1
# def showDate(Y,M,D):
#     print(Y,"年",M,"月",D,"日")

# y = input("誕生年を入力。")
# m = input("誕生月を入力")
# d = input("誕生日を入力")
# showDate(y,m,d)

# 演習2
# def showDate():
#     y = int(input("誕生年を入力。"))
#     m = int(input("誕生月を入力"))
#     d = int(input("誕生日を入力"))
#     print(y,"年",m,"月",d,"日")

#     n = int(input("今年何年"))
#     AGE = n - y
#     return AGE

# age = showDate()
# print(age,"才です")

###演習6

##6-1
# def showDate(year,month,day):
#     print(year,"年",month,"月",day,"日")

# year = int(input("誕生年を入力してください。"))
# month = int(input("誕生月を入力してください。"))
# day = int(input("誕生日を入力してください。"))
# showDate(year,month,day)



# ##6-2
def showAge(year):
    age = 2020-year
    print(age,"才です。")

def showDate(year,month,day):
    print(year,"年",month,"月",day,"日")
    showAge(year)

year = int(input("誕生年を入力してください。"))
month = int(input("誕生月を入力してください。"))
day = int(input("誕生日を入力してください。"))
showDate(year,month,day)



# ##6-3
# def rpast(num):
#     print("*" * num)

# num = int(input("個数を入力してください。"))
# rpast(num)

# #以下でも可
# for i in range(num):
#     print("*",end="")

# num = int(input("個数を入力してください。"))
# rpast(num)



# ##6-4
# def rpstr(num,str="*"):
#     for i in range(num):
#         print(str,end="")
#     print("")

# str = input("文字列を入力してください。")
# num = int(input("個数を入力してください。"))

# if str == "":
#     rpstr(num)
# else :
#     rpstr(num,str)