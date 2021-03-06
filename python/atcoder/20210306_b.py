
"""
Nで以降にinputする行を確定させる
A, Bそれぞれリスト単位で出力する
それぞれ仕事としての最小値を出す
それらの最小値のインデックスが同じであれば、リストから抜いて合計値を足す、再度リストの中で
最小値を出して比較、これをリスト内のものがなくなるまで繰り返す
"""

#時間切れ、模範解答

# 第一引数をnにおいている(jobs)
n = int(input())
# range(n)何行分繰り返すか(jobsの数)を指定し、第二引数以降を格納している
for i in range(n):
    """
    map関数は加工元を第二引数に示し、それをどのように加工するかという部分を
    第一引数によって指定する。関数で処理するなど、今回はint型にしている
    """
    a,b = map(int,input().split())
    # 最小値比較
    # 最小値を投入、合計値を投入
    if i==0:
        minA = a
        minB = b
        sumAmin = sumBmin = a+b
    # 仕事Aの値が低かったらminA,Aindex,sumAminを更新している
    # sumAminは仮にAの値が最小値を更新した場合に同じworkerのBと合計をとっている
    # sumBminはelifだからaのほうで更新がかかったらスキップされる
    if a<minA:
        minA = a
        sumAmin = a+b
    elif b<minB:
        minB = b
        sumBmin = a+b
print(minA,minB,sumAmin,sumBmin)
print (min(max(minA,minB),min(sumAmin,sumBmin)))