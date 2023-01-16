# P124 コンストラクタ
class Character:
    # コンストラクタ設定
    def __init__(self, name, level):    #インスタンス実行時nameにはドラゴン、levelには50が入る
        self.name = name
        self.level = level
    
    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level

# ↓のインスタンス実行時に4行目のコンストラクタが動く
chara = Character("ドラゴン", 50)
print("NAME:", chara.getName(), ",LEVEL", chara.getLevel())