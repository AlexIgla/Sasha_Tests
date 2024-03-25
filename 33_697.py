#Ремонт
l, w, h = list(map(int, input().split()))
s = 2 * h * (w + l)
a = 16
if s % a == 0:
    print(int(s // a))
else:
    print((s // a + 1))