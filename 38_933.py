#Телефон
a, b, c, t = list(map(int, input().split()))
if t <= a:
    print(t * b)
elif t > a:
    print(a * b + (t-a) * c)