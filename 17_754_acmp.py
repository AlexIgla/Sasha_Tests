#Три толстяка
m1, m2, m3 = map(int, input().split())
if min(m1,m2,m3) < 94 or max(m1,m2,m3) > 727:
    print('Error')
else:
    print(max(m1, m2, m3))
