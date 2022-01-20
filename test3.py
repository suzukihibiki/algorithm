





from collections import deque

a = deque(["Ram", "Tarun", "Asif", "John"])


while a:
    
    b , c= a.popleft()
    print(b,c)