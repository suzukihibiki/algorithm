





def main(value):
    if value <= 1:
        return False
    for j in range(2, int(value**0.5) + 1):
        if value % j == 0:
            return False
    return True

test_data = 11

A = main(value=test_data)

print(A)