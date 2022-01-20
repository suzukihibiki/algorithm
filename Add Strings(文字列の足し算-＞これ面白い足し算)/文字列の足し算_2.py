
num1 = '8'
num2 = '100'

def solution(num1, num2):
    
    n1, n2 = 0, 0
    m1 = 10**(len(num1)-1) # 1文字1 2文字10 3文字100 4文字1000
    m2 = 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)
num = solution(num1, num2)
print(num)