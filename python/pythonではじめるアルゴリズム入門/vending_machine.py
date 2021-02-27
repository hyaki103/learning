import sys # エラー時に強制終了するためのモジュール

"""
順に考えると…
# お釣りの金額を求める

insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

# 5000円札の枚数を求める
r5000 = change // 5000
q5000 = change % 5000
print('5000: ' + str(r5000))

# ...以下1円まで同様の処理を繰り返す
"""

insert_price = input('insert: ')
if not insert_price.isdecimal():
    print('整数を入力してください')
    sys.exit()
product_price = input('product: ')
if not product_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

change = int(insert_price) - int(product_price)
if change < 0:
    print('金額が不足しています。')
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10 ,5, 1]

"""
for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))
"""
"""
pythonにはdivmod関数があり、divmod(a, b)は(a // b, a % b)を返す
"""
for i in coin:
    r, change = divmod(change, i)
    print(str(i) + ': ' + str(r))
