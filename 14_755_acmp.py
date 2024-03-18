#Сбор земляники
x, y, z = map(int, input().split())
s = x+y-z
if s < 0:
    print('Impossible')
else:
    print(s)