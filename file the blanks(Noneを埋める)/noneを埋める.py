array1 = [1,None,2,3,None,None,5,None]

def solution1(array):
    valid = 0
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

def solution2(array):
    last = 0
    for i in range(len(array)):
        if array[i] is None:
            array[i] = last
        else:
            last = array[i]
    return array

print(solution1(array1)) # => [1, 1, 2, 3, 3, 3, 5, 5]
print(solution2(array1)) # => [1, 1, 2, 3, 3, 3, 5, 5]