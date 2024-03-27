#Треугольник - 3
a, b, c = list(map(int, input().split()))
if a < b + c and c < b + a and b < a + c:
    print('YES')
else:
    print('NO')