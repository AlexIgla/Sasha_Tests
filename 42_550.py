#День программиста
a = int(input())
b = 0
if a<10:
    b='000'+str(a)
elif a<100:
    b = '00'+str(a)
elif a<1000:
    b = '0'+str(a)
else:
    b = a
a = int(b)
if a%400 == 0 or(a%4==0 and a%100!=0):
    print(f"12/09/{b}")
else:
    print(f'13/09/{b}')
