#Прямоугольный параллелепипед
a, b, c = map(int, input().split())
s = (a * c + a * b + b * c) * 2
v = a * b * c
print(s, v)
