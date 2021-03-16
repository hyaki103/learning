#　いろいろな探索

# 線形探索　順番に調べるだけなのでプログラムの構造が非常にシンプル
# ex.) リストから目的の値を探すプログラム

"""変数で状態管理を行う
data = [50, 30, 90, 10, 20, 70, 60, 40, 80]


found = False # 見つかっていない状態をセットしておく
for i in range(len(data)):
    if data[i] == 40:
        print(i + 1)
        found = True
        break
if not found:
    print('Not Found')
"""

# 関数として定義して使用する

def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 40))

# 二分探索
"""
線形探索と比較して、対数のペースで比較回数が増加するため、
データ数が1000個程度に増えても比較回数は10回程度
(線形探索はO(n))
計算量はO(logn)
※事前にデータの並べ替えが必要
"""

def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
        # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else: 
            right = mid - 1
    return -1
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))

# 木構造での探索
"""
階層構造になっているデータを探索する場面を考える
ex.) sample.txtという名前のファイルを一覧にする
→幅優先探索と深さ優先探索
幅優先探索：目次→それぞれの章の概要→章の内容
深さ優先探索：目的のほうへ進めるだけ進み、進めなくなったら戻る
すべての答えを見つけるときによく用いられ、オセロや将棋、囲碁などの探索で用いられる
★メモリ使用量を抑えられるのは深さ優先探索
→幅優先探索は途中のノードをすべて保持する必要があるが、深さ優先探索は現在のノードを保持しておくだけでよい
★高速なのは幅優先探索
→見つかった時点で処理を終了できる、深さ優先探索は全ノードを調べてから最短か判定する必要がある
"""

# 木構造をリスト形式で表現する

#tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], []]

#★動かん…
"""
data2 = [0]
while len(data2) > 0:
    pos = data2.pop(0)
    print(pos, end='')
    for i in tree[pos]:
        print(i)
        data2.append(i)
"""
# 深さ優先探索
"""
この辺動かん、とばし
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], []]
print(tree[0])
def search(pos):
    print(pos, end='')
    for i in tree[pos]:
        search(i)
search(0)

"""