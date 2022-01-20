



def prime_num(n):
    p = [i for i in range(n + 1)]
    for i in p[3:]:
        if p[i] % 2 == 0:
            p[i] = 0
    root_n = n ** 0.5
    for i in range(3, n):
        if i > root_n:break
        if p[i] != 0:
            for j in range(i, n + 1, 2):
                if i * j >= n + 1:break
                p[i * j] = 0
                    
               
    plist = sorted(list(set(p)))[2:]
    return plist


test_data = 50

plist = prime_num(test_data)

print("n以下の素数は", plist)
plistn = str(len(plist))+'個'
print(plistn)