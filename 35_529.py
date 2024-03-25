#Длина отрезка
x1, y1, x2, y2 = list(map(int, input().split()))
print(int((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
