class Cookie:
    count = 0

    def __init__(self, type):
        Cookie.count += 1
        self.type = type

    @classmethod
    def getCount(cls):
        return cls.count

    @classmethod
    def cookieStart(cls):
        print("クッキーを作ります")

    def getType(self):
        return self.type

#クラスのインスタンス生成前にメソッド呼び出し
Cookie.cookieStart()

#クラスのインスタンス生成
cookies = [Cookie("メープル"), Cookie("抹茶"), Cookie("チョコ")]

#クラス変数の表示
print("カウンター:", Cookie.getCount())

#インスタンス変数の表示
for c in cookies:
    print(c.getType())