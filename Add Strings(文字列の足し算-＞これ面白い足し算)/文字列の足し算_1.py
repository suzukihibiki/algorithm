num1 = '100'
num2 = '8000'

# Approach 1: 
def solution(num1,num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))

print(solution(num1,num2))
