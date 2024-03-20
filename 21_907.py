#Мышка
w, h, r = map(int, input().split())
sp = w * h
sk = 3.14 * r ** 2
if r*2 <= h and r*2 <= w:
    print('YES')
else:
    print('NO')