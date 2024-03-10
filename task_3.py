import random
n = 30
N = [random.randint(-100, 100) for i in range(n)]


c = 0
cnt = 0
max_cnt = 0
while c != len(N)-1:
    if N[c] < N[c+1]:
        cnt+=1
        max_cnt = max(cnt, max_cnt)
    else:
        cnt = 1
    c+=1

print(N)
print(max_cnt)