#Конечные автоматы
k = int(input())
for i in range(k):
    n, m = map(int, input().split())
    d = 19 * m + (n + 239) * (n + 366) / 2
    if d % 1 == 0:
        print(int(d))
    else:
        print(d)