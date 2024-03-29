



# 素数
# ==========================================================================================================================

# 約数が 1 とその数自身だけであるような自然数を素数と言います。例えば、最初の8 つの素数は2, 3, 5, 7, 11, 13, 17, 19 となります。1 は素数ではありません。

# n 個の整数を読み込み、それらに含まれる素数の数を出力するプログラムを作成してください。

# 注意 : 素数の数を求める。


# 入力
# ==========================================================================================================================
# 最初の行に n が与えられます。続く n 行に n 個の整数が与えられます。


# 出力
# ==========================================================================================================================
# 入力に含まれる素数の数を１行に出力してください。


# 入出力例
# ==========================================================================================================================
# <in>
# 6
# 2
# 3
# 4
# 5
# 6
# 7
# <out>
# 4


# 取得
# ==========================================================================================================================
# 形式 => H が S の要素数
# H
# S1
# ・
# ・
# ・
# SH

# Sample
# 5
# 100
# 100
# 500
# 500
# 500


# コード例3 : 
H = map(int, input().split())
S = [input() for _ in [0] * H]


# 基本形 ※実際に動きます。
# ==========================================================================================================================


# 解説
# ==========================================================================================================================


# 独自
# ==========================================================================================================================

ans = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a == 2:
        ans += 1
    elif a%2 == 0:
        continue
    else:
        if pow(2, a-1, a) == 1:
            ans += 1
print(ans)

# 計算速度 ※実際に動きます。
# ==========================================================================================================================
from multiprocessing.sharedctypes import Value
import sys
input()
print(sum(2 in[x,pow(2,x,x)]for x in map(int,sys.stdin)))





ans = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a == 2:
        ans += 1
    elif a%2 == 0:
        continue
    else:
        if pow(2, a-1, a) == 1:
            ans += 1
print(ans)

# メモリ
# ==========================================================================================================================

# コードサイズ ※実際に動きます。
# ==========================================================================================================================
import sys
input()
print(sum(2 in[x,pow(2,x,x)]for x in map(int,sys.stdin)))






# 汎用モデル : 速度,コードサイズ優先 : リスト内の素数の数
# ==========================================================================================================================

# 1
"""
args
---
value : list
    対象のリスト

return
---
value : int
    引数のリストにあった素数の数。
"""
def main(value):
    value = (sum(2 in[x,pow(2,x,x)]for x in value))
    return value
test_data = [6,2,3,4,5,6,7]
ancer_data = main(
    value = test_data
)
print(ancer_data)

# 汎用モデル : イメージのしやすさ優先 : リスト内の要素の数
# ==========================================================================================================================
"""
args
---
value : list
    対象のリスト

return
---
value : int
    引数のリストにあった素数の数。
"""

def main(value):
    ans = 0
    for i in value:
        if i == 2:
            ans += 1
        elif i%2 == 0:
            continue
        else:
            if pow(2, i-1, i) == 1:
                ans += 1
    return ans

test_data = [6,2,3,4,5,6,7]
ancer_data = main(
    value = test_data
)
print(ancer_data)

    
# 汎用モデル : 素数かいなかの判定
# ==========================================================================================================================
"""
args
---
value : list
    対象のリスト

return
---
value : int
    引数のリストにあった素数の数。
"""

def main(value):
    if value <= 1:
        return False
    for j in range(2, int(value**0.5) + 1):
        if value % j == 0:
            return False
    return True

test_data = [6,2,3,4,5,6,7]
for i in test_data:
    ancer_data = main(
        value = i
    )
    print(f"{i} : {ancer_data}")