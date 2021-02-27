# UMLの作成はgitmind
"""
n = 18

result = ""

while n > 0:
    result = str(n % 2) + result
    n //= 2

print(result)
"""
# 10進数を他進数に変換
n = 18

def convert(n, base):
    result = ""

    while n > 0:
        # 基数で割った余りを右からつけていく
        result = str(n % base) + result
        # 基数で割った商をnに再代入
        n //= base
    
    return result

print(convert(n, 2))
print(convert(n, 5))

# 2進数を10進数に変換する
n = '10010'

result = 0
for i in range(len(n)):
    print(n[i])
    result += int(n[i]) * (2 ** (len(n) - i - 1))
print(result)

"""
多くの言語ではこういった進数の変換は関数が用意されている。
10→2　bin()
2→10 int(x, 2)
"""

# 先頭に0bをつけると整数型の値として処理できる
print(0b10010)