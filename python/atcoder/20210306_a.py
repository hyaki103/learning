"""
乳固形分が 
15
 パーセント以上、乳脂肪分が 
8
 パーセント以上含まれるもの
 乳固形分は無脂乳固形分と乳脂肪分の 
2
 つから成ります
"""
# splitでスペースの入ってる位置で変数を区切る
no_nyuu, on_nyuu = input().split()
fat = int(on_nyuu)
kokei = int(no_nyuu) + fat

if kokei >= 15 and fat >= 8:
    print('1')
elif kokei >= 10 and fat >= 3:
    print('2')
elif kokei >= 3:
    print('3')
else:
    print('4')