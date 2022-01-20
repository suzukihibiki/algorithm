# 1から昇順で数えたときに、N番目にあたる素数を出力するコマンドラインツールを作成してください。
# 入力：出力したい素数の順番 N
# 出力：N番目の素数



def main(value):
    if value <= 1:
        return False
    for j in range(2, int(value**0.5) + 1):
        if value % j == 0:
            return False
    return True

def prime_seq(cnt):
    i = 1
    while 0 < cnt:
        i += 1
        if main(i):
            cnt -= 1
    return i


print('1番目の素数：',prime_seq(1))
print('5番目の素数：',prime_seq(5))