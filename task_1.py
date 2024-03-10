def deleting(indexes, currsum):
    flag = 1
    for i in range(len(indexes)):
        if v[i] == currsum:
            v.pop(i)
            w.pop(i)
            break
        else:
            for j in range(len(indexes)):
                if v[i]+v[j] == currsum:
                    v.pop(i)
                    w.pop(i)
                    v.pop(j-1)
                    w.pop(j-1)
                    flag = 0
                    break
        if flag == 0:
            break


v = []
w = []

Weight = int(input("Ввеите грузоподъемность: "))
count = int(input("Введите количество заходов: "))

while True:
    s1 = input("Введите стоимость экспоната: ")
    s2 = input("Введите его вес: ")
    if (s1 != '') and (s2 != ''):
        v.append(int(s1))
        w.append(int(s2))
    else:
        break

summ = 0

k = 0
while (k < count) and (len(v) > 0):
    m = []
    for i in range(len(v)):
        m.append([])

    for i in range(len(v)):
        for j in range(Weight + 1):
            m[i].append(0)

    indexes = set()
    for i in range(len(v)):
        for j in range(Weight + 1):
            if (w[i] > j):
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - w[i]] + v[i])
                if (m[i][j] == m[i - 1][j - w[i]] + v[i]):
                    indexes.add(i)

    indexes = list(indexes)
    indexes.sort()
    summ_numb = m[len(m) - 1][len(m[0]) - 1]
    summ += m[len(m) - 1][len(m[0]) - 1]
    deleting(indexes, summ_numb)
    k+=1

print(summ)
#5000+2500+1000+1500+1250



