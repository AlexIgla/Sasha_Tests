#Будильник
s, t = list(map(int, input().split()))
if s > t:
    print(t + 12 - s)
else:
    print(t - s)