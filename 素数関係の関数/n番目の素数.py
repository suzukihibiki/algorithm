

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

test_data = 1
test_data_2 = 5

print('1番目の素数：',prime_seq(test_data))
print('5番目の素数：',prime_seq(test_data_2))