#Кондиционер
tr, tc = list(map(int, input().split()))
x = input()
y = 0
if x == 'heat' and tr > tc:
    print(tr)
elif x == 'heat' and tr <= tc:
    print(tc)
elif x == 'freeze' and tr > tc:
    print(tc)
elif x == 'freeze' and tr <= tc:
    print(tr)
elif x == 'auto':
    print(tc)
else:
    print(tr)