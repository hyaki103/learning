import sys
# 閏年を産出する
uruu = []
for i in range(1950, 2051):
    # 100で割り切れて、400で割り切れない年は閏年ではない
    if i % 100 == 0 and i % 400 != 0:
        continue
    # 4で割り切れる年は閏年
    elif i % 4 == 0:
        uruu.append(i)
    else:
        continue

print(uruu)

# 西暦の都市が引数で与えられたとき、元号に変換して出力する関数を作成する
n = input('西暦を入力してください：')
def seireki(n):
    if not n.isdecimal():
        print('整数で入力してください')
        sys.exit()
    year = int(n)
    if year < 1869 or year > 2020:
        print('1869年から2020年までの年号を入力してください')
    elif year >= 2019:
        print(f"令和{year - 2019 + 1}年")
    elif year >= 1989:
        print(f"平成{year - 1989 + 1}年")
    elif year >= 1926:
        print(f"昭和{year - 1926 + 1}年")
    elif year >= 1912:
        print(f"大正{year - 1912 + 1}年")
    else:
        print(f"明治{year - 1868 + 1}年")

seireki(n)
