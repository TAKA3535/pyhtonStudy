# 複数のインスタンス
class Character:
    def getName(self):
        return self.name

    def getLevel(self):
        return self.level
    
# インスタンスの作成(↓は3個作成してる)
Characters = [Character(),Character(),Character()]
Characters[0].name = "ゴブリン"
Characters[1].name = "ドラゴン"
Characters[2].name = "スライム"
Characters[0].level = 12
Characters[1].level = 50
Characters[2].level= 9999

for chara in Characters:
    print("名前:", chara.getName(), "level:", chara.getLevel())