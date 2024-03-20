#Золотой песок
a1, a2, a3, b1, b2, b3 = map(int, input().split())
c = max(a1, a2, a3)
d = max(b1, b2, b3)
money1 = c * d
e = min(a1, a2, a3)
f = min(b1, b2, b3)
money2 = e * f
g = (a1 + a2 + a3) - (max(a1, a2, a3) + min(a1, a2, a3))
h = (b1 + b2 + b3) - (max(b1, b2, b3) + min(b1, b2, b3))
money3 = g * h
print(int(money1 + money2 + money3))