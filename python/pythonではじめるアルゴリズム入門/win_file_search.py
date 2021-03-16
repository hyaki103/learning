import os
for i in os.listdir('/'):
    #対象がディレクトリか調べる
    print(i + ':' + str(os.path.isdir('/' + i)))

"""
権限を調べる
os.access関数
1つ目の引数にはディレクトリやファイルの名前を、２つ目の引数には調べる内容を指定する
os.F_OK 存在するかどうか
os.R_OK 読み込み可能かどうか
os.W_OK 書き込み可能かどうか
os.X_OK 実行可能かどうか
"""

# 深さ優先探索
def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(dir + i + '/', name)

# アクセス拒否される為お蔵
#search("C:\\Users\\", 'alias')

print(os.access("C:\\Users\\hyaki\\OneDrive\\デスクトップ", os.R_OK))