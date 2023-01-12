# 5-15 タプルP85
tuple = ("国語", "算数", "理科", "社会")
print("tuple:",tuple)
print("tuple[1]:",tuple[1])
print("tuple[2:]:",tuple[2:])
print("tuple[::-1]:",tuple[::-1])

# 参照している変数に再代入
tuple = ("英語", "体育", "音楽", "美術")
print("tuple:",tuple)

# 以下のプログラムはエラーになります。
# tuple[0] = "美術"