







# <in>
# 5 100
# p1 150
# p2 80
# p3 200
# p4 350
# p5 20

# <out>
# p2 180
# p5 400
# p1 450
# p3 550
# p4 800


# Python code to demonstrate Implementing 
# Stack using deque
# from collections import deque
# queue = deque(["Ram", "Tarun", "Asif", "John"])
# print(queue)
# queue.append("Akbar") # enqueue
# print(queue)
# queue.append("Birbal")
# print(queue)
# print(queue.pop()) # dequeue    
# print(queue.pop()) # dequeue       
# print(queue)




from collections import deque



# def main(q, t_w):
#     d = deque(t_w)
#     l = []
#     time = 0
#     while d: # dの要素が無くなるまで実行
#         k, v = d.popleft() 
#         if v > q:
#             v -= q # タスクのウェイト(時間)を引く(1回のクオンタム100ms分s)
#             time += q # 都度、クオンタムを追加。
#             d.append([k,v])
#         else:
#             time += v
#             l += [f'{k} {time}']
#     return l

# # n, q = map(int, input().split())
# # task_name_wight = [0] * n
# # for i in range(n):
# #     task_name_wight[i] = map(int, input().split())
    
    
# q = 100
# task_name_wight = [("p1",150), ("p2",80),("p3", 200)]
# ancer_data = main(
#     q = q,
#     t_w = task_name_wight
# )
# print(*ancer_data,sep="\n")









def main(q, t, w):
    t_d = deque(t)
    w_d = deque(w)
    l = []
    time = 0
    while t_d: # dの要素が無くなるまで実行
        k = t_d.popleft()
        v = w_d.popleft()
        print(v)
        print(q)
        if v > q:
            v -= q # タスクのウェイト(時間)を引く(1回のクオンタム100ms分s)
            time += q # 都度、クオンタムを追加。
            t_d.append(k)
            w_d.append(v)
        else:
            time += v
            l += [f'{k} {time}']
    return l

# n, q = map(int, input().split())
# task_name = [0] * n
# task_weight = [0] * n

# for i in range(n):
#     task_name[i], task_weight[i] = input().split()
    
# task_weight = list(map(int ,task_weight))

q = 100
task_name = ["p1", "p2","p3"]
task_weight = [150, 80, 200]

ancer_data = main(
    q = q,
    t = task_name,
    w = task_weight
)
print(*ancer_data,sep="\n")