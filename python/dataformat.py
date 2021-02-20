# 数値型
"""
int: 整数 ex.)3
float: 少数 ex.)3.5
complex: 複素数 ex.)2.3j
"""

# シーケンス型
"""
list: リスト ex.)[1, 2, 3]
tuple: タプル  ex.)(1, 2, 3)
range: 範囲 ex.)range(10)
"""

# 論理型
"""
bool: 真偽 ex.) True, False
"""

# テキストシーケンス型
"""
str: 文字列 ex.) 'abc'
"""

# バイトシーケンス型
"""
byte: ASCII 文字列 ex.)b'abc'
"""

# 集合型
"""
set: 集合 ex.) {'one', 'two'}
"""

# 辞書型
"""
dict: 辞書(連想配列) ex.){'one': 1, 'two': 2, 'three': 3}
"""
# クラス
"""
class: クラス ex.) Math
"""

print(type('str'))
print(type(2+3j))

# 変数として使える文字
"""
1文字目はアルファべット or アンダースコア
2文字目以降はアルファベット or 数字 or アンダースコア
長さに制限はなく、大文字と小文字は区別される
予約語を変数として使用することが出来ない
アンダースコアから始まる変数は特別な意味がある
"""

# pythonのコーディング規約 → PEP-8
"""
変数名として小文字だけを使い、複数の単語を使う場合には区切りとしてアンダースコアを使用する
単独でアンダースコアのみを変数に使用した場合は、
「その変数を後の処理で使わないから無視してよい」
といった特殊な意味がある
"""

# リストとリスト内の要素取得
a = [3, 1, 4, 2, 5]
print(a[1:3])
print(a[2:])
print(a[:3])
print(a[:-3])

# タプル →　要素の変更が不可、リストより高速、値の変更の心配がない
b = (1, 2, 4, 5, 6)
print(type(b))

# 文字と文字列
print('abcdefg'[-3:])
print('abcd'+'efg')
# 文字列の中に数値を埋め込む
print('abc%i' % 123)


# 比較演算子
"""
a is b
a is not b
a in b
a not in b
"""

a = 15
if (a >= 10) and (a < 20):
    print('10 <= a < 20')
else:
    print('a < 10 or 20 <= a')

# long_sentence
long_name_variable = 1
if (long_name_variable == 1111111111111111111111111111) \
or (long_name_variable == 222222222222222222222222222) \
or (long_name_variable == 3333333333333333333333333333) :
    print('long value')

# long_list
url_list = [
    'https://test.com',
    'https://www.shoeisha.co.jp'
    'http://webshop.com'
]

# 繰り返し
for i in range(4, 7):
    print(i)

# 位置と値を格納する
for i, e in enumerate([5, 3, 7]):
    print(i, ':', e)

# リスト内包表記
"""
リストの生成、操作をシンプルに実装する
内包表記を使うほうが処理が高速になることがある
"""
data_new = [i for i in range(10)]
print(data_new)

# リスト内包表記じゃない書き方↓
data = []
for i in range(10):
    data.append(i)

print(data)

# 条件の指定もできる
data_new2 = [i for i in range(10) if i % 2 == 0]
print(data_new2)
"""
if~elseと条件を満たさない場合にも処理する場合は、
if説とfor文が入れ替わる
data = [i if i % 2 == 0 else 0 for i in range(10)]
"""