
# TODO:	あとで追加、修正するべき機能がある。

# HACK:	あまりきれいじゃないコード。リファクタリングが必要。

# REVIEW:	意図した通りに動くか、見直す必要がある。

# NOTE:	なぜ、こうなったという情報を残す。



# ==========================================================================================================================

# import math
# x , p = str(input()).split()
# def calculation(x_,p_) -> int:
#     i = x_
#     while x_ != 0:
#         x_ = math.floor(x_ - ((x_ * p_) / 100))
#         i += x_
#     return i



# a = calculation(int(x),int(p))
# print(a)


# リファクタリング==========================================================================================================================

# 解き方手順マニュアルに
# 1.問は何が知りたいか
# 問の答えは「合計なんぼで、0になるか」

# 2.必要な計算式
# 今回は、[割引(%)を求める計算式,累計の計算式]が分かれば良い。

# 3.必要なルーチンの洗い出し。
# {
    # 割引価格計算ルーチン : 割引価格を計算するルーチン
    # 累計ルーチン : 累計を計算するルーチン
    # 小数点以下切り捨てるルーチン : 小数点以下切り捨てるルーチン
# }

# 4.必要となるルーチンのハードコーディングか、関数か、クラスかを決定する
# ※関数、クラスの時は、引数、戻り値を記載。
# {
    # 割引価格ルーチン ： 関数(再利用性が高い)
    # 累計 :  ハードコーディング
    # 小数点以下切り捨て : ハードコーディング
# }

# 5.UI的なアーキテクチャの作成
# 具体的にどのように呼び出すか。…コーディングで示すので、文章では割愛

# 6.各関数を具体的に決める。


# コーディング手順
# 1.解き方手順マニュアル4の値のルーチンを記載。

import math

_value, _percent = str(input()).split()
_value = int(_value)
_percent = int(_percent)

def calculation(value_ : int ,percent_ : int) -> int:
    _value = value_ - ((value_ * percent_) / 100)
    return _value

# 累計演算子ではなく、リストで保管してラストにsum関数
total_value = [_value]
add_value = total_value.append


while _value!= 0:
    _value = math.floor(
        calculation(
            value_=_value,
            percent_=_percent
        )
    )
    add_value(_value)

total_value = sum(total_value)
print(total_value)