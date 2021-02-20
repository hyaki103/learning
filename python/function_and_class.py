# 関数とクラス
"""
関数の定義
def 関数名(引数):
    実行する処理
    返す値
"""

def add(a, b):
    return a + b

print(add(3, 5))

"""
変数の有効範囲
ローカル変数：関数の中など、一部からしかアクセスできない変数
エンクロージングスコープ変数：関数の外側にあるローカル変数(関数の中で関数を定義する場合などに使われる)
グローバル変数：ファイルの中でどこからでもアクセスできる変数
ビルトイン変数：lenやrangeといったどこからでもアクセスできるもの
"""

"""
クラスの定義
class クラス名:
    def メソッド名(引数):
        処理内容

    def メソッド名(引数):
        処理内容
"""

class User:
    # コンストラクタ、オブジェクト生成時に必ず呼び出され、オブジェクトが扱うデータなどを初期化するために使われる。反対にデストラクタも存在する。
    def __init__(self,name,password):
        self.name = name
        self.password = password
    
    def login(self, password):
        if self.password == password:
            return True
        else:
            return False
    
    def logout(self):
         print('logout')

a = User('admin','password')
if a.login('password'):
    a.logout()
