# Монетки
a = int(input())
i, n, m = 0, 0, 0
while i < a:
    b = int(input())
    i += 1
    if b == 0:
        n += 1
    else:
        m += 1
print(min(n, m))
