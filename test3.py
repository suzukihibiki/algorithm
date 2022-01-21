





from collections import deque

a = deque([["Ram", 1],["aaaaa",2]])


while a:
    
    b , c= a.popleft()
    print(b)
    print(c)