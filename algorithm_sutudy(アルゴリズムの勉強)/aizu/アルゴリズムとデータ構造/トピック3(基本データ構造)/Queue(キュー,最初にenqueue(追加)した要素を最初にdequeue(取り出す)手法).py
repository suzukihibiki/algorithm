



# キュー
# ==========================================================================================================================

# 名前 name(i) と必要な処理時間 time(i) を持つ n 個のプロセスが順番に一列に並んでいます。
# ラウンドロビンスケジューリングと呼ばれる処理方法では、CPU がプロセスを順番に処理します。
# 各プロセスは最大 q ms（これをクオンタムと呼びます）だけ処理が実行されます。
# q ms だけ処理を行っても、まだそのプロセスが完了しなければ、そのプロセスは列の最後尾に移動し、CPU は次のプロセスに割り当てられます。

# 例えば、クオンタムを 100 msとし、次のようなプロセスキューを考えます。

# A(150) - B(80) - C(200) - D(200)
# まずプロセス A が 100 ms だけ処理され残りの必要時間 50 ms を保持しキューの末尾に移動します。

# B(80) - C(200) - D(200) - A(50)
# 次にプロセス B が 80 ms だけ処理され、時刻 180 ms で終了し、キューから削除されます。

# C(200) - D(200) - A(50)
# 次にプロセス C が 100 ms だけ処理され、残りの必要時間 100 ms を保持し列の末尾に移動します。

# D(200) - A(50) - C(100)
# このように、全てのプロセスが終了するまで処理を繰り返します。

# ラウンドロビンスケジューリングをシミュレートするプログラムを作成してください。






# 入力
# ==========================================================================================================================
# n q
# name(1) time(1)
# name(2) time(2)
# ・
# ・
# ・
# name(n) time(n)

# 最初の行に、プロセス数を表す整数 n とクオンタムを表す整数 q が１つの空白区切りで与えられます。

# 続く n 行で、各プロセスの情報が順番に与えられます。文字列 namei と整数 timei は１つの空白で区切られています。

# 出力
# ==========================================================================================================================
# プロセスが完了した順に、各プロセスの名前と終了時刻を空白で区切って１行に出力してください。

# 制約
# ==========================================================================================================================
# 1 <= n <= 100,000
# 1 <= q <= 1,000
# 1 <= time(i) <= 50,000
# 1 <= 文字列 name(i) の長さ <= 10
# 1 <= timei の合計 <= 1,000,000


# 入出力例
# ==========================================================================================================================
# <in>
# 5 100
# p1 150
# p2 80
# p3 200
# p4 350
# p5 20
# <out>
# p2 180
# p5 400
# p1 450
# p3 550
# p4 800




# 独自理解
# ==========================================================================================================================
# 1から順にタスクが実行され、実行されるごとに、100クオンタムかかります。
# そして、終わった順にかかった時間を出力

# 取得
# ==========================================================================================================================
# 形式 => N が t の要素数
# N M
# t1 x1
# t2 x2
# ・
# ・
# ・
# tN xN

# Sample
# 6 4 => 縦の要素が6個ある
# 1 2
# 2 3
# 1 4
# 1 2
# 2 3
# 15 4

# コード
N, M = map(int, input().split())
t = [0] * N
x = [0] * N
for i in range(N):
    t[i], x[i] = map(int, input().split())
    


# 基本形 ※実際に動きます。
# ==========================================================================================================================


# 解説
# ==========================================================================================================================


    
    
# 計算速度 ※実際に動きます。
# ==========================================================================================================================
import sys
from collections import deque
def m():
    s = sys.stdin.readlines()
    q = int(s[0].split()[1])
    
    f = lambda x,y:(x,int(y))
    
    d = deque(f(*e.split())for e in s[1:])
    t, a = 0, []
    while d:
        k, v = d.popleft()
        if v > q: 
            v -= q
            t += q
            d.append([k,v])
        else:
            t += v
            a += [f'{k} {t}']
    print('\n'.join(a))
if'__main__'==__name__:m()





# UI性重視
# ==========================================================================================================================
from sys import stdin
from collections import deque

input = stdin.readline
inputs = stdin.readlines

def solve(n, q, P):
    P = deque(P)
    t = 0
    while P:
        p = P.popleft()
        if p[1] <= q:
            t += p[1]
            print(p[0], t)
        else:
            p[1] = p[1] - q
            P.append(p)
            t += q
    
def main():
    n, q = map(int, input().split()) 
    P = [list(input().split()) for _ in range(n)]
    P = [[p, int(t)] for p, t in P]
    solve(n, q, P)

if __name__ == '__main__':
    main()


# コードサイズ ※実際に動きます。
# ==========================================================================================================================



















# 汎用モデル : 速度優先
# ==========================================================================================================================

from collections import deque

q = 100
task_name_weight = (["p1",100],["p2",200],["p3",300])

def main(q, t_w):
    t_w = deque(t_w)
    add_t_w = t_w.append
    l = []
    time = 0
    while t_w: # dの要素が無くなるまで実行
        k,v = t_w.popleft()
        v = int(v)
        if v > q:
            v -= q # タスクのウェイト(時間)を引く(1回のクオンタム100ms分s)
            time += q # 都度、クオンタムを追加。
            add_t_w([k,v])
        else:
            time += v
            l += [f'{k} {time}']
    return l

ancer_data = main(
    q = q,
    t_w = task_name_weight
)
print(*ancer_data,sep="\n")

# 汎用モデル : ライブラリ無しver
# ==========================================================================================================================

