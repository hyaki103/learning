"""
フィボナッチ数列とは？
直前の2つの項を足し合わせてできる数列のこと
1,1,2,3,5,8,13,,,と続く
"""
"""
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(200):
    print(fibonacci(i), end=" ")
"""

"""
↑の処理はfibonacchi(n)を何度も何度も呼び出すため、数が多くなるほど時間がかかる
→「メモ化」を使用して高速化
"""

memo = {1: 1, 2: 1} # 辞書に終了条件の値を入れる

def fibonacchi(n):
    if n in memo:
        return memo[n] # 辞書に登録されていればその値を返す

    memo[n] = fibonacchi(n -2) + fibonacchi(n - 1) # メモになければ計算して登録する

    return memo[n]

print(fibonacchi(200))
print(memo)