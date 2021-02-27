# 素数を判定する

import math
"""
def is_prime(n):
    
    1以下は素数ではないため、最初に判定をしてFalseを返す
    2以上の場合は、2からその数の平方根までループを繰り返し、割り切れるかを判定する
    割り切れた場合は素数ではない
    いずれの数でも割り切れなかった場合は素数と判定し、Trueを返す
    for文で+1しているのはrangeが最後の数を含めないため
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(200):
    if is_prime(i):
        print(i, end=" ")
"""

# 効率よく素数を求める「エラトステネスの篩」
"""
2の倍数、３の倍数、、、と徐々に倍数を除外していくことで素数だけを残す
"""

def get_prime(n):
    if n <= 1:
        return []
    prime  = [2]
    limit = int(math.sqrt(n))

    # 奇数のリストを作成
    data = [i + 1 for i in range(2, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        # 割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]

    return prime + data

print(get_prime(200))

# 実際に素数を扱う場合はsympyというライブラリを読み込む
